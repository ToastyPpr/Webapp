# Webapp (Flask Web Application)

A web application built using Python and Flask.

---
## IMPORTANT: Ai is permited to use on this project but ONLY FOR DEBUGGING everything else has to be done 
## by hand, the use of AI can lead to many issues in the future espeically if we plan on deploying
## Prerequisites

Before running this project, make sure you have the following installed:
* **Python 3.10+** (Added to System PATH)
* **VS Code** (Recommended IDE)
* **Git**

---

## Quick Start / Setup Instructions

Follow these steps to set up and run the application locally on your machine.

### 1. Clone the Repository
```bash
git clone <YOUR-REPOSITORY-URL>
cd Webapp


### 2. Create the virtual env for this project in vscode terminal 
    python -m venv .venv

### 3. activate the Virtual env.
    .\.venv\Scripts\Activate.ps1

            ## Side notes if using powershell: If script execution is disabled, run Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser once. (This needs to be done once in your powershell)

### 4. installing dependencies
    pip install -r requirements.txt

### 5 Run the app

        python app.py
### Structurally we should look like this for the following project,comments are a must, needs to be clean and easy to read almost as if you are reading to a child 
Webapp/
├── .venv/               # Isolated Python virtual environment (ignored by Git)
├── instance/            # holds the database data for the current instance
├── static/              # CSS styles, images, JavaScript files
├── templates/           # HTML templates rendered by flask
    ├────Admin/
        /base_admin.html
        /dashboard.html 
        /leads.html
        /reviews.html     
├── app.py               # Main Flask application entry point
├── database.py          # Holds database information and how it works
├── requirements.txt     # List of required Python packages
└── README.md            # Project documentation and setup guide


# Auguest 23 2026

worked on the submit button, so far it works (i did mess up the css on the form but will work on it tomorrow), form works well. I believe we can start working ont he sql db.

## August 25 2026 

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


