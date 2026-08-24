import os
from flask import Flask
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
    return render_template("index.html", portfolio_items=PORTFOLIO_ITEMS)
# testing before we implement into sqldatabase
LEAD_LIST = []
# SCRIPT FOR SUBMITTING QUOTE FORM
@app.route("/submit-quote", methods=["POST"])
def submit_quote():
    client_name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    details = request.form.get("details")


# Storing data in a dictionary for demonstration purposes

    lead_data = {
        "name": client_name,
        "phone": phone,
        "email": email,
        "details": details
    }

    LEAD_LIST.append(lead_data)

    print("\n--- A new Lead has been submitted ---\n")
    print(f"client {client_name} | Phone: {phone} | Email: {email} | Details: {details}")

    return jsonify({
        "status": "success",
        "message": f"Thank you, {client_name}! Your quote request has been submitted successfully."
    }), 200

    # Here, you can implement logic to store the quote_data in a database or perform any other necessary actions.

    # For demonstration, we'll just return a success message.
    return jsonify({"message": "Quote submitted successfully!", "data": quote_data}), 200

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port=5000, debug=True)



