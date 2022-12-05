# URLshort Django
Accepts a URL and returns a shortened version.  Takes a shortened url and returns the original longer URl

## Prerequisites:
  * asgiref==3.5.2
  * Django==4.1.3
  * sqlparse==0.4.3
  * Sqlite3 1.4 

# Local Installation
* Clone this repo ([instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))
* Navigate into this project's directory `cd url_short_django`
* Create a virtual environment $ `python3 -m venv myvenv`
* Start virtual environment $ `source myvenv/bin/activate`
* Install Django $ `python3 -m pip install django`
* Create migrations $ `python3 manage.py makemigrations`
* Migrate $ `python3 manage.py migrate`
* Start the local server by running $ `python3 manage.py runserver`
* View by visiting `http://127.0.0.1:8000` in a web browser


## Database

SQLite3 would work in development but we don't recommend running it in production. Instead look into using the built-in [Replit database](http://docs.replit.com/misc/database). Otherwise you are welcome to connect databases from your favorite provider. 

