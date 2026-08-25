import os
from flask import Flask #  <<< I dont think this is required -Ben
from flask import Flask, render_template, request, jsonify
from database import db, Lead, initialize_database

app = Flask(__name__)
#starts DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///triple_j.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
initialize_database(app)

PORTFOLIO_ITEMS = [
    {
        "title": "Custom home Build",
        "category": "custom builds",
        "description": "This is a web development project.",
        "image": "project1.jpg"
    },
    {
        "title": "Porch addition",
        "category": "Addition",
        "description": "This is an app development project.",
        "image": "project2.jpg"
    },
    {
        "title": "Bathroom remodel",
        "category": "Design",
        "description": "This is a design project.",
        "image": "project3.jpg"
    },
    {
        "title": "Kitchen renovation",
        "category": "Remodel",
        "description": "This is a kitchen renovation project.",

        "image": "project4.jpg"

    },
    {
        "title": "Deck Construction",
        "category": "Custom Builds",
        "description": "This is a deck construction project.",
        "image": "project5.jpg"
    }
]

# network config

@app.route("/")
def home():
    return render_template(
        "index.html",
        portfolio_items=PORTFOLIO_ITEMS
    )


@app.route("/submit-quote", methods=["POST"])
def submit_quote():
    client_name = (request.form.get("name") or "").strip()
    phone = (request.form.get("phone") or "").strip()
    email = (request.form.get("email") or "").strip()
    details = (request.form.get("details") or "").strip()

    if not client_name or not phone or not email:
        return jsonify({
            "status": "error",
            "message": "Name, phone, and email are required fields."
        }), 400

# Storing data in a dictionary for demonstration purposes

    new_lead = Lead(
        name=client_name,
        phone=phone,
        email=email,
        details=details
    )

    db.session.add(new_lead)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": f"Thank you, {client_name}! Your quote request has been submitted successfully."
    }), 200


if __name__ == "__main__":
    app.run(host = "0.0.0.0",port=5000, debug=True)



