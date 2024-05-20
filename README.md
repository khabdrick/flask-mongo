# Flask Blog Application

## Overview

This project is a Flask-based blog application demonstrating two versions: one using SQLite with SQLAlchemy and the other using MongoDB with Flask-PyMongo. The application allows users to create, edit, view, and delete blog posts, as well as search for posts.

## Features

- Create, edit, and view blog posts
- Delete blog posts
- Search for blog posts by title or content


### Flask App with SQLite

1. Navigate to the SQLite version directory:
    ```bash
    cd flask-sql
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:
    ```bash
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    ```

4. Run the application:
    ```bash
    python run.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000/home`.

### Flask App with MongoDB

1. Navigate to the MongoDB version directory:
    ```bash
    cd flask_app_mongodb
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up MongoDB:
    - Make sure MongoDB is installed and running on your local machine.
    - Update the `MONGO_URI` in `config.py` if necessary.

4. Import sample data (optional):
    ```bash
    python import_json_to_mongo.py
    ```

5. Run the application:
    ```bash
    python run.py
    ```

6. Open your browser and navigate to `http://127.0.0.1:5000/home`.

### `config.py`

#### SQLite Version

```python
import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

#### MongoDB Version

```python
import os

class Config:
    SECRET_KEY = os.urandom(24)
    MONGO_URI = 'mongodb://localhost:27017/blogdb'
```



