# URLshort Django
Click Here to see the live site https://ushort.up.railway.app

Accepts a URL and returns a shortened version. Takes a shortened url and returns the original longer URL.

_Time spent: 3h._

## Prerequisites:
  * asgiref==3.5.2
  * Django==4.1.3
  * sqlparse==0.4.3
  * Sqlite3 1.4 

# Local Installation
* Clone this repo ([instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))
* Navigate into this project's directory `cd url_short_django`
* Create a virtual environment `python3 -m venv myvenv`
* Start virtual environment `source myvenv/bin/activate`
* Install Django `python3 -m pip install django`
* Create migrations `python3 manage.py makemigrations`
* Migrate $ `python3 manage.py migrate`
* Start the local server by running `python3 manage.py runserver`
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

## Creating base template following DRY principles 
<img width="1456" alt="dry" src="https://user-images.githubusercontent.com/89544506/205586402-8f07b3ce-728b-456d-9bf0-24d43be01aff.png">

## Paths urls.py
<img width="1075" alt="Screen Shot 2022-12-05 at 12 18 19 AM" src="https://user-images.githubusercontent.com/89544506/205587735-c1a372fd-35fa-4f1e-a45d-795c500dd1a5.png">


## CreateShortURL method for POST and GET request
<img width="1406" alt="create" src="https://user-images.githubusercontent.com/89544506/205586762-93fa5761-428a-4813-8fab-28755aade699.png">

## URL Restorer and Redirect
<img width="1157" alt="restore" src="https://user-images.githubusercontent.com/89544506/205587369-b291d04c-0524-4be3-be2a-d6be62aef2b8.png">


