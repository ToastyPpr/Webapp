import os
from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from database import db, Lead, initialize_database

app = Flask(__name__)

# Application configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///triple_j.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["BOOKING_URL"] = "https://calendar.app.google/WGgDvPj6xebfbCaQ9"


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


@app.route("/thank-you")
def thank_you():
    """Show confirmation and scheduling options after a saved quote."""

    return render_template(
        "thank_you.html",
        booking_url=app.config["BOOKING_URL"]
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

    new_lead = Lead(
        name=client_name,
        phone=phone,
        email=email,
        details=details
    )

    db.session.add(new_lead)
    db.session.commit()

    return redirect(url_for("thank_you"))


if __name__ == "__main__":
    app.run(host = "0.0.0.0",port=5000, debug=True)



