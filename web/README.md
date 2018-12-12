# tourney-beast
Youth sports tournaments rating web application

##Setup:
<pre><code>
$ git clone git@github.com:calebho/tourney-beast.git
$ virtualenv virtual-environment-name 
$ source virtual-environment-name/bin/activate
$ cd tourney-beast
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
</code></pre>

In your browser, navigate to localhost:8000.
After the initial setup, you only need to run the following
in order to start the production server.

<pre><code>
$ source virtual-environment-name/bin/activate
$ cd tourney-beast
$ python manage.py runserver
</code></pre>
