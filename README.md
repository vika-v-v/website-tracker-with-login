# Website change tracker
This bot helps to track the website change on it's source code. I am using it to get the email nontification when the exam grades are published as my university doesn't send email nontifications explicitly.

# How to install
Use `git clone https://github.com/vika-v-v/website-tracker-with-login`, then change variables to your paramethers:  
>- url of the website you want to track  
>- login_url : url of the login page  
>- your login data: login and password (make sure not to post the changed data to the Internet)  
>- check interval in seconds (currently set to hourly)  
>- email login, so the nontification-email will be sent  
>- recipient email (can be the save email as above)  
  
Then you need to start the script in order for the bot to work.  

Type `python website_monitor.py` in cmd  

**or set bot autostart:**

For Unix-based systems (like Linux or Mac)

You can use Cron jobs to schedule scripts. Cron is a time-based job scheduler in Unix-like operating systems. To open the crontab configuration file, you'd open your terminal and type:

`crontab -e`

This will open the crontab file where you add your jobs. Let's say you want to run your script every hour, you might add a line like this:

`0 * * * * /usr/bin/python3 /path/to/your/script.py`


For Windows systems

You can use Task Scheduler:

1. Open Task Scheduler. You can find it by searching in the Start menu.

2. Click "Create Basic Task..."

3. Name your task and click "Next".

4. Choose "On start" and click "Next".

5. Choose "Start a program" and click "Next".

6. Click "Browse..." and navigate to your Python executable. If you installed Python from python.org, it might be in a location like `C:\Python39\python.exe` (your path could vary, check your Python installation location). In the "Add arguments (optional)" field, put the path to your script, like `C:\path\to\your\script.py`. Click "Next".

7. Click "Finish".


The script will only track changes when your pc is on.
