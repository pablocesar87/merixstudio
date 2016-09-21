Project for merixstudio interview


#INSTALLATION GUIDE

##IMPORTANT:
You need to have redis in your machine in order to celery to work properly.
Installing redis in Ubuntu is really easy: sudo apt-get install redis-server
To check if server is running properly run: redis-cli ping; it should answer:PONG

##IMPORTANT 2:
The application assumes that you already have a database named "merixstudio" with PostgreSQL.
You will have to fill the database settings in your local.py created from your local_template.py
with your own data.

"settings/local.py" should be created from "merixstudio/settings/local_template.py". Just fill with your information.

##STEPS:
    ·Create a virtualenv for python3: python3 -m venv "yourvenvname"

    ·Install dependencies: pip install -r requirements/base.txt

    ·Execute migrations: python manage.py migrate

    ·Start your local server: python manage.py runserver



##The next step is very important in order to the site to work properly

To start celery to work, you need to start a new worker, to do so you need to follow the next steps:

    -Open a new terminal

    -Start your virtual environment in this new terminal

    -Go to your project folder(merixstudio folder)

    -Once inside the folder run: celery -A merixstudio worker -l info