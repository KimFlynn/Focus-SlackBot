from slackclient import SlackClient
import time
 
slack_client = SlackClient('xoxb-873400785666-885730484036-Cgw6ApEfj8IxWoGe7SS8XMTs')
 
if slack_client.rtm_connect(with_team_state=False):
    print ("Successfully connected, listening for events")
    while True:
        print(slack_client.rtm_read())
         
        time.sleep(1)
else:
    print("Connection Failed")