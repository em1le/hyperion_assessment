# Demo application (second task)

The application look up for files within dropbox root folder, store data from those files and create a chart to display how many times a user modifies its files.

## Getting Started

You need to have a valid dropbox token to go to the next step

### Prerequisites

1. Python 3.6
2. Virtualenvwrapper

Docker is optional.
If you do not want to use docker replace ```DATABASES``` in tracker/settings.py

Replace the following code:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST')
    }
}
```

with this:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
```

3. Docker
4. Docker-compose

The following command must be type in your bash.

Check if Python 3.6 is installed:
```
python --version
```

If not follow this [link](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04)

Now check that you have virtualenvwrapper installed:
```
virtualenvwrapper
```

If not:
```
sudo apt install virtualenvwrapper
```

If docker and docker-compose are already installed on your local machine you can pass.
If not follow this [link](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04)


### Installing

#### Clone the project
```
git clone git@github.com:em1le/hyperion_assessment.git
```
then

```
cd second_task/
```

#### Set up virtualenvwrapper

```
mkvirtualenvwrapper second_task
```

then

```
pip install -r requirements.txt
```

#### Launch docker-compose
```
sudo docker-compose -f docker-compose.yml up
```

#### Set up you dropbox token
Go to the tracker folder and open .env file
and change the line DROPBOX_TOKEN with yours
```
DROPBOX_TOKEN=your_dropbox_token
```

#### Run the migration command
```
./manage.py migrate
```

#### Test if your app is ok
```
./manage.py check
```
From now you app should work without any problems.

### How does it work?

You can check how many times a user modified its files in 3 ways:

1 - In running the django management command:
```
./manage.py check_filedata
```

2 - In creating a django crontab:
```
./manage.py manage.py crontab add
```
The settings of django crontab are available in django setting file

3 - Using the interface
![alt text](https://github.com/em1le/hyperion_assessment/blob/master/peek_ok.gif "Interface")



## Built With

* [Django](https://www.djangoproject.com/) - The python framework used
* [Chartit](https://github.com/chartit/django-chartit) - module to create charts
* [Django cron](https://github.com/kraiz/django-crontab) - module to create django cron

