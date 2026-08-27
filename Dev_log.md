# Possible to do list

-Style the CSS a little more

-Add real project photos/ descriptions. 

-obtain logo

-navigation links

-add thank you message to submit button

-database may need to handle errors a little more gracefully

-add spam protection

-Page description

-business phone and service area

-business structured data

-Google Business Profile 

-sitemap and search console

-make scheduling addon to website for customers

## In order to deploy we need to

-protect customer data (database)

-Finish required website content

-Finish the quote form and round it out

-prepare the DB 

-Basic Cybersecurity practices need to be implemented


## Auguest 23 2026 - Alex

worked on the submit button, so far it works (i did mess up the css on the form but will work on it tomorrow), form works well. I believe we can start working ont he sql db.

## August 25 2026 - Ben

Added SQLite database storage using Flask-SQLAlchemy. and fleshed out the endpoint in the app.py

The database code is located in `database.py`. The `Lead` model stores the customer's name, phone number, email, and project details. When the app starts, it automatically creates the database at:

```text
instance/triple_j.db
```

When the quote form is submitted:

```text
Quote form → Flask route → Lead object → SQLite database
```

Testing the Database

1. Start the application:

```powershell
python app.py
```

2. Open `http://127.0.0.1:5000` and submit a test quote.

3. Check the saved leads:

```powershell
python -c "import sqlite3; db=sqlite3.connect('instance/triple_j.db'); print(db.execute('SELECT * FROM lead').fetchall())"
```

If the submitted information appears, the database is storing leads correctly.
