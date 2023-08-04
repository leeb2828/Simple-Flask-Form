# Simple Flask Form

This project was forked from https://github.com/leeb2828/Simple-Flask-Form
- HTML 
- CSS 
- Python 
- Flask (micro web framework) 
- Flask SQLAlchemy (Flask extension for managing database) 
- Flask-WTF. It is a built-in module of flask which allows for designing forms in your application, so you don't have to hard code everything in your
  HTML file.
- Sqlite database.
- Dockerfile
 
<br />

![Form Page](images/formpage.png)

<br />
A "Than you for Registering" page will display, and the user will have the option of entering a new user or viewing the entire database of people. 
<br />

![Submitted Page](images/thankyou.png)

<br />
On the database page, the user can delete or modify a person's information. 
<br/>

![Database Page](images/the_database.png)

<br /><br />
### Local run
Download the files using the git clone command.
```
$ git clone <link to project>
```
Create your virtual environment
```
$ python3 -m venv env
$ source env/bin/activate
```
You can run locally by 
```
$ pip install -r requirements.txt
```
Run the app.py file
```
$ python3 app.py
```
Type in http://localhost:5000 into your browser to view the project live.
 
### Or you can run the docker container
```
./docker.sh
http://0.0.0.0:5000/
```



