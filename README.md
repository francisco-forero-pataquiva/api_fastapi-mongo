# Back-end Challenge 🏅 2021 - Space Flight News

This is a challenge by <a href = "https://coodesh.com/">Coodesh</a>

## About 

This REST API project was made as a back-end challenge for Coodesh. The API was centered around CRUD operations using data from the <a href = "https://api.spaceflightnewsapi.net/v3/documentation">Space Flight News API</a> stored in a MongoDB database. The database was populated using a daily CRON that scrapped the available data and kept it up to date.

### Stack 

The API was written using Python 3.9 with FastApi as the framework and MongoDB as the database. 
To perform in an asynchronous fashion the database operations, the motor library was chosen. 
For the populator and scrapper, the requests library was used. 
For the CRON, both the schedule and time libraries were used.

### Installing

Use the following commands to create a virtual environment on your Linux/Mac:

```
python3 -m venv venv
source venv/bin/activate
```

To install the dependencies of the project, use this command:

```
python3 -m pip install -r requirements.txt
```

To start the API, just run the main.py file, and to start the CRON, run cronjob.py.

NOTE: It's important to notice that here I've included a .env file to facilitate the testing of the project, but this wouldn't be recommended in production environments.

