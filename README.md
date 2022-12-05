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

## Create a shortened URL version

![ezgif com-gif-maker (4)](https://user-images.githubusercontent.com/89544506/205569158-0e8aea0b-0ebc-4b25-b627-c534ffdf4af3.gif)

## Takes a shortened url and returns the original longer URL

![ezgif com-gif-maker (5)](https://user-images.githubusercontent.com/89544506/205570775-9c675131-acff-410b-9e7a-47af7260bd4e.gif)



## Database

SQLite3 would work in development but we don't recommend running it in production. Instead look into using the built-in [Replit database](http://docs.replit.com/misc/database). Otherwise you are welcome to connect databases from your favorite provider. 

## Models

- to create model ⇒ from src run python3 [manage.py](http://manage.py) makemigrations
- python3 [manage.py](http://manage.py/) migrate  to create all the necessary tables in the DB

<img width="884" alt="model" src="https://user-images.githubusercontent.com/89544506/205585914-b0aa5f0d-6634-4465-a29f-7f47d5e31049.png">


