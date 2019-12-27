# Focus-SlackBot
A slack bot which allows for easy on task management, lists, and other management strategies.

In order to use, a few slack packages must be installed: `slackbot`, `websocket`, `slackclient`, and `slacker`.
To install, place items in the same directory and use `pip install packagename`

This project began on 12/25/2019. The ReadMe and files will continue to be updated until the final product is released.

## Key Functions
This bot has several key functions:
- `/subject` allows users to set a meeting subject along with key words. If the subject or key words are not mentioned after 25 comments, the bot will send a reminder of the subject.

- `/endSubject` will turn this function off. All topic reminders will stop.

- `/timer` allows users to set a meeting timer.

- `/agenda` allows users to set a meeting agenda check list. Users can type agenda at any time to see meeting agenda objectives. Users can also delete agenda objectives. 

- `/list` allows users to set a Todo list with a due date and critical scale. If critical, the user will be reminded every day of the objective until checked off. Todo items with due dates within 3 days (customizable) or less will also be reminded. Weekly reminders will also be set to remind users of completed and upcoming weekly tasks.

- `/Google` allows users to search items without leaving slack in order to keep up with conversations and allow for easy fact checking.

