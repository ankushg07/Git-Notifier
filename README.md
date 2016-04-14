# Git Notifier


>This project sends an SMS with details of notification you received on Github

##Requirments
* Twilio Account
* Github Api Access token
* VM/Server for cronjob


####To setup a **cronjob**

Type: _crontab -e_ in terminal

Enter the time setting for cronjob as following per format

_* * * * * /your/directory/Script_

where " * " depicts 

minute hour day month day-of-week repectively from left to right
