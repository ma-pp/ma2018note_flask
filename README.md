# ma2018note_flask
The apps for sharing notes with others, or use it for yourself. We will add chat feature in future.

The project is sub-app from Muslim Apps Project

# Prequisites
First, make sure you have `python3` with `pipenv` installed.

To install `pipenv` you need to install `pip`.
If you haven't had `pip`, install it with these:
```
$ sudo apt-get install python3-pip
```

Then install `pipenv`:
```
$ python3 -m pip install pipenv
```

# How to setup
For the first time run, go to project directory and type this command:
```
$ python3 -m pipenv install
```

For the next run and so on, everytime you want activate the virtual environment, go to project directory and type this command:
```
$ python3 -m pipenv shell
```

# How to run
After activating virtual environment, run this command to run the project:
```
$ flask run
```

# API Swagger Documentation
After you run `flask` in 'How to run' section open `127.0.0.1:5000/api` in your browser to see swagger documentation.


# Contributing
If you find any bug or you have any advice, please contact me at `wiyonoagung1@gmail.com`.