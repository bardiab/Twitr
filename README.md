## 8x8 Take Home Challenge

A system that allows to both write and read logs via an API into a database.

### Prerequisites

Create a virtualenv and please make sure that you have all the dependencies listed in requirements.txt

### Background

I built a small app to show posts(twits) by a user, built in python using the Flask framework. I have never worked with Flask before, so it was an interesting challenge. There are different API endpoints when navigating the site, and anytime an action is performed by the user, this is logged into a table called "Log" and located in the posts.db file.

When finished navigating the application, logs may be viewed under the "Log" table in a sql visualizer of your choosing.
The log database has rows for logger, level, trace, msg, and when the log was created.

### Installing

After downloading the project, in order to get the server up and running on your local host, first setup a virtual environment from the base Twitr directory:

1. Check to see if conda is installed
```
conda -V
```
2. If not, run
```
pip install conda
```

3. Create a virtual environment
```
conda create -n yourenvname python=3.6.3 anaconda
```

4. Activate virtual environment
```
source activate yourenvname
```

5. Make sure you have all packages required
```
pip install -r /path/to/requirements.txt
```

6. Now, in order to get the app up and running run:
```
python app.py
```

From there you can log in to the website on your local machine and view posts using username 'bardia' and password 'lol'.
```
http://127.0.0.1:5000/
```


### Requirements

- **Completeness**: Wrote multiple API endpoints, wrote multiple tests covering these endpoints, used git for version control, and also stored both my website data and log data in a sql database using SQLAlchemy.
- **Correctness**: Basic functionality works as expected, except as I expanded the project, I realized that my test breaks because of circular imports, and realized that in order to remedy the issue I would likely have to refractor my entire project structure. After some unsuccessful debugging I decide in the interest of time I would submit first and attempt to fix it later.
- **Reasoning**: In order to tackle such a vague project on something I don't have much experience, I set about doing some research and settled on using Flask to build my app in. After reading up on the documentation and looking into some basic guides, I was able to get my app up and running.

### Built With

* [Atom](https://atom.io) - TextEditor
* [Bootstrap](https://getbootstrap.com) - HTML/CSS Framework
* [Flask](http://flask.pocoo.org) - Framework
* [SQLAlchemy](https://www.sqlalchemy.org) - Database
