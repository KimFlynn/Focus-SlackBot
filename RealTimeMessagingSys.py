from slackclient import SlackClient
import time
 
slack_client = SlackClient('xoxb***')
 
if slack_client.rtm_connect(with_team_state=False):
    print ("Successfully connected, listening for events")
    while True:
        print(slack_client.rtm_read())
         
        time.sleep(1)
else:
    print("Connection Failed")
