## 8x8 Take Home Challenge

A system that allows to both write and read logs via an API into a database.

### Prerequisites

Create a virtualenv and please make sure that you have all the dependencies listed in requirements.txt

### Background

I built a small app to show posts(twits) by a user, built in python using the Flask framework. I have never worked with Flask before, so it was an interesting challenge. There are different API endpoints when navigating the site, and anytime an action is performed by the user, this is logged into a table called "Log" and located in the posts.db file.

When finished navigating the application, logs may be viewed under the "Log" table in a sql visualizer of your choosing.

### Installing

After downloading the project, in order to get the server up and running on your local host, run:

```
python app.py
```

From there you can log in to the website and view posts using the username 'bardia' and the password 'lol'.


### Requirements

- **Completeness**: Wrote multiple API endpoints, wrote multiple tests covering these endpoints, used git for version control, and also stored both my website data and log data in a sql database using SQLAlchemy.
- **Correctness**: Basic functionality works as expected
- **Reasoning**: In order to tackle such a vague project on something I don't have much experience, I set about doing some research and settled on using Flask to build my app in. After reading up on the documentation and looking into some basic guides, I was able to get my app up and running.

### Built With

* [Atom](https://atom.io) - TextEditor
* [Bootstrap](https://getbootstrap.com) - HTML/CSS Framework
* [Flask](http://flask.pocoo.org) - Framework
* [SQLAlchemy](https://www.sqlalchemy.org) - Database
