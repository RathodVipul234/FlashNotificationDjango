#Flash Notification Project Setup


1. Create Virtualenv
```shell
  python3 -m venv venv
```


2. Activate venv 

```shell
  source venv/bin/activate
```


3. Install requirement.txt file
```shell
  pip install -r requirement.txt
```

4. Makemigrations
```shell
  python3 manage.py makemigrations
```
5. Migrate
 ```shell
  python3 manage.py migrate
```
7. create super user for accessing admin panel
```shell
  python3 manage.py createsuperuser
```

5. register user from registration form and login with that user

6. Schedule New notification from admin panel and start celery servers. you can follow bellow staps



#Setup celery

1. start celery beat server
```commandline
celery -A FlashNotification beat -l INFO
```
2. start celery worker server
```commandline
celery -A FlashNotification.celery worker -l INFO
```

3. start django_celery_beat.schedulers server
```commandline
celery -A FlashNotification beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

4. start django_celery_beat.schedulers server with debug mode
```commandline
celery -A FlashNotification beat --loglevel=debug --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
