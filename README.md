# Sofia Swing Dance Festival
## Quick install guide

1. Prerequisites

  - Python 3.5
  - [SpatiaLite](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/install/spatialite/#homebrew)

2. Install SpatiaLite (for local development)
  ```
  $ brew install geos
  $ brew install spatialite-tools
  $ brew install gdal
  ```
3. Setup django requirements
  ```
  $ pip3 install -r requirements.txt
  $ python3 manage.py makemigrations
  $ python3 manage.py migrate
  ```

4. Create superuser, follow instructions to enable write access and manage oauth applications
  ```
  $ python3 manage.py createsuperuser
  ```

5. Run the server locally
  ```
  $ python3 manage.py runserver
  ```

6. Login
7. To access oauth navigate to: `serverurl/oauth2/applications/`

  https://django-oauth-toolkit.readthedocs.org/en/latest/tutorial/tutorial.html

## Deploying on Heroku
[Try Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
or follow these few steps:

1. Install Heroku toolbelt
2. Login to Heroku

  ```
  heroku login
  Enter your Heroku credentials.
  Email: python@example.com
  Password:
  ...
  ```

3. Deploy
  Create an Heroku app

  ```
  heroku create
  Creating lit-bastion-5032 in organization heroku... done, stack is cedar-14
  http://lit-bastion-5032.herokuapp.com/ | https://git.heroku.com/lit-bastion-5032.git
  Git remote heroku added
  ```

  **DOKKU**

  If you're using dokku instead of heroku, install dokku-apt plugin:
  `https://github.com/F4-Group/dokku-apt`

  And then setup GIS extension for Postgres

  ```
  Use the docker command to pull the image you want:

  (sudo) docker pull mdillon/postgis:latest
  Then just set your env vars:

  export POSTGRES_IMAGE="mdillon/postgis"
  export POSTGRES_IMAGE_VERSION="latest"
  Then you just use the plugin to create a new database.
  ```

  Now deploy your code:

  ```
  git push heroku master
  Counting objects: 232, done.
  Delta compression using up to 4 threads.
  Compressing objects: 100% (217/217), done.
  Writing objects: 100% (232/232), 29.64 KiB | 0 bytes/s, done.
  Total 232 (delta 118), reused 0 (delta 0)
  remote: Compressing source files... done.
  remote: Building source:
  remote:
  remote: -----> Python app detected
  remote: -----> Installing python-2.7.11
  remote:      $ pip install -r requirements.txt
  remote:        Collecting dj-database-url==0.4.0 (from -r requirements.txt (line 1))
  remote:          Downloading dj-database-url-0.4.0.tar.gz
  remote:        Collecting Django==1.9.2 (from -r requirements.txt (line 2))
  remote:          Downloading Django-1.9.2-py2.py3-none-any.whl (6.6MB)
  remote:        Collecting gunicorn==19.4.5 (from -r requirements.txt (line 3))
  remote:          Downloading gunicorn-19.4.5-py2.py3-none-any.whl (112kB)
  remote:        Collecting psycopg2==2.6.1 (from -r requirements.txt (line 4))
  remote:          Downloading psycopg2-2.6.1.tar.gz (371kB)
  remote:        Collecting whitenoise==2.0.6 (from -r requirements.txt (line 5))
  remote:          Downloading whitenoise-2.0.6-py2.py3-none-any.whl
  remote:        Installing collected packages: dj-database-url, Django, gunicorn, psycopg2, whitenoise
  remote:          Running setup.py install for dj-database-url: started
  remote:            Running setup.py install for dj-database-url: finished with status 'done'
  remote:          Running setup.py install for psycopg2: started
  remote:            Running setup.py install for psycopg2: finished with status 'done'
  remote:        Successfully installed Django-1.9.2 dj-database-url-0.4.0 gunicorn-19.4.5 psycopg2-2.6.1 whitenoise-2.0.6
  remote:
  remote:      $ python manage.py collectstatic --noinput
  remote:        58 static files copied to '/app/gettingstarted/staticfiles', 58 post-processed.
  remote:
  remote: -----> Discovering process types
  remote:        Procfile declares types -> web
  remote:
  remote: -----> Compressing...
  remote:        Done: 39.3M
  remote: -----> Launching...
  remote:        Released v4
  remote:        http://lit-bastion-5032.herokuapp.com/ deployed to Heroku
  remote:
  remote: Verifying deploy... done.
  To git@heroku.com:lit-bastion-5032.git
   * [new branch]      master -> master
  ```

  The application is now deployed. Ensure that at least one instance of the app is running:

  ```
  $ heroku ps:scale web=1
  ```

  Now visit the app at the URL generated by its app name. As a handy shortcut, you can open the website as follows:

  ```
  $ heroku open
  ```
