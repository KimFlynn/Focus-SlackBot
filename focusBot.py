from slackclient import SlackClient
import time
slack_client = SlackClient('xoxb-')

class slackCommunication(object):
    def __init__(self):
        self.slack_client = slack_client
        self.appName = "FocusBot"

    #connects to slack using code
    def slackConnect(self):
        return self.slack_client.rtm_connect()

    #reads messages
    def slackReadRTM(self):
        while True:
            print(self.slack_client.rtm_read())
            time.sleep(1)

    #get users, text, members, and channel
    def parseSlackInput(self, input, botID):
        botATID = "<@" + botID + ">"
        input = input[0]
        if botATID in input['text']:
            user = input['user']
            message = input['text'].split(botATID)[1].strip[' ']
            channel = input["channel"]
            return [str(user), str(message), str(channel)]
        else:
            return [None, None, None]
            
    def getBotID(self, botusername):
        api_call = self.slack_client.api_call("users.list")
        users = api_call["members"]
        for user in users:
            if 'name' in user and botusername in user.get('name') and not user.get('deleted'):
                return user.get('id')

    def writeSlack(self, channel, message):
        return self.slack_client.api_call("chat.postMessage", channel = channel, text = message, as_user = True)

class mainFun(slackCommunication):
    def __init__(self):
        super(mainFun, self).__init__()
        BOTID = self.getBotID[self.appName]
    
    def decideActionPlace(self, input):
        if input:
            user, message, channel = input
            return self.writeSlack(channel, message)
        
    def run(self):
        self.slackConnect
        BOTID = self.getBotID(self.appName)
        while True:
            self.decideActionPlace(self.parseSlackInput(self.slackReadRTM(), BOTID))
            time.sleep(1)
        
    if __name__ =="__main__":
        instance = mainFun()
        instance.fun()
