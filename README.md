# Jims-CS532
Jail Information Management System project repository.

## Set Up Python

Download Anaconda
https://store.continuum.io/cshop/anaconda/

Their Python distribution is free and has all the dependencies needed except for some web dev stuff.
Be sure to allow them to set Anaconda as your default Python.

# Clone this repo and install web dependencies
Assuming you have git run the following

```
git clone https://github.com/humdings/Jims-CS532.git
cd Jims-CS532
pip install -r requirements.txt
```

Alternatively, download the zip file, unpack it, then run the last 2 commands


We will be making a [Django](https://www.djangoproject.com/) app for this project.
[Mezzanine](http://mezzanine.jupo.org/) is a Django project that comes with a lot 
of pre-built stuff, including css/html templates for the website, I think we should
use that project as our jump off point.

#Running the development server
While still in the project directory run the following
```
python manage.py createdb --noinput
python manage.py runserver
```

If the planets are aligned you should have a local server running the project. 
The default username is 'admin' and the password is 'default'

Go to http://your localhost/admin to see the admin stuff, 
we will basically be customizing the admin pages to make the JIMS project.


