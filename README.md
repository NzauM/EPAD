# EPAD
An online tool for monitoring and evaluating employees.
>[Nzau~Mercy](https://github.com/NzauM)  
  
# Description  
EPAD is an online tool for monitoring and evaluating employees.A manager who needs to be logged in as a super user can access 
the dashboard 
##  Live Link  
 Click [Nzauhood](https://nzaupad.herokuapp.com)  to visit the site
  
 
## User Story  
  
### Manager
* Log in to the dashboard.
* Assign Taks to employees
* Rate employees according to performance 
* Check employee logs and activities
### Employee
* Sign up and log intoo the system
* See my profile information
* See tasks assigned to me 
* See task collaborators if any
* See my rates in various fields and overall ratings.

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/NzauM/EPAD.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd HoodWatch 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations epad
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 2.2.6](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Support and contact details
 For any issues ,contact at https://github.com/NzauM/EPAD/issues <br>
 Or for any pull requests, https://github.com/NzauM/EPAD/pulls
  Incase you need more clarification, feel free to send an email to: 
Email: mercywaenu16@gmail.com
  
## License 


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/NzauM/Instagram/blob/master/LICENSE)
MIT License
\_ **Nzau Mercy @2020**
