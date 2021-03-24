# social_network
This is a set of API's for Post model.
There are documented api calls: https://documenter.getpostman.com/view/11733536/TzCHAAFz

## Features
This project has such abilities as:
* User registration API
* User can have access to APIs only after authentication (using jwt token)
* ONLY super admin user can have access to activity API, which will have info about last user login
* CRUD model for Post instance
* see details of only one instance using its id
* Post can be liked or disliked

## Instalation
To launch this project first you need to clone the repository.

```bash
git clone 'repository link'
```

create virtual environment and activate it

```bash
python3 -m venv <name of virtual env folder>
source <name of virtual env folder>/bin/activate
```
After thet you can install all dependencies

```bash
pip3 install -r requirements.txt 
```

Create super user to have access to User activity endpoint

```bash
python3 manage.py createsuperuser
```

After that you can run the server

```bash
python3 manage.py runserver
```

Here you should be good to go. 

