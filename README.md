# ZHU / ZTL Information Display System

An information display system

Written in Python 3 using the Django web framework.

By Michael Romashov and Jake Greenbaum.

## Prerequisites
- Python 3.8+
- [Docker Desktop](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)

## Installation
Before you begin, make sure you clone the repository into an accessible directory.
### Redis
Run the following commands in command prompt as an admin user, location does not matter.
1. `docker pull redis`
2. `docker run --name ids-redis -p 6378:6378 -d redis`
    - Redis will now be available at `127.0.0.1:6378`.

Use `docker container stop ids-redis` when you want to stop the Docker container.
### Django
Run the following commands in command prompt as an admin user from within the cloned repository.
1. `python -m venv venv`
2. `venv\Scripts\activate`
   - You should see `(venv)` next to your command line location.
3. `pip install -r requirements`
4. `python manage.py makemigrations`
5. `python manage.py migrate`
6. `python manage.py runserver`
    - The website can now be accessed at `localhost:8000`.