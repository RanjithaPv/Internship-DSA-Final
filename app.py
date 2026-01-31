from flask import Flask, render_template, request
import numpy as np
from genai import genai_advisor

app = Flask(__name__)

# Dummy prediction logic (NO model.pkl needed)
def predict_success(features):
    score = (
        features["rating"] * 2 +
        min(features["students_enrolled"] / 1000, 5) +
        min(features["reviews_count"] / 100, 3)
    )
    return round(score, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    suggestions = []

    if request.method == "POST":
        course = {
            "course_title": request.form["course_title"],
            "price_usd": float(request.form["price_usd"]),
            "rating": float(request.form["rating"]),
            "students_enrolled": int(request.form["students_enrolled"]),
            "reviews_count": int(request.form["reviews_count"]),
            "category": request.form["category"],
            "difficulty_level": request.form["difficulty_level"]
        }

        prediction = predict_success(course)
        suggestions = genai_advisor(course, prediction)

    return render_template(
        "index.html",
        prediction=prediction,
        suggestions=suggestions
    )

if __name__ == "__main__":
    app.run(debug=True)
