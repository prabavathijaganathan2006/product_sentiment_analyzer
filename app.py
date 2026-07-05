from flask import Flask, jsonify, request
from flask_cors import CORS
from flipkart_scraper import scrape_flipkart
from sentiment import analyze_sentiment
from database import save_review, get_reviews

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend Running Successfully"


@app.route("/search")
def search():

    product = request.args.get("product")

    try:
        reviews = scrape_flipkart(product)

        result = []

        for review in reviews:
            sentiment = analyze_sentiment(review)

            save_review(review, sentiment)

            result.append({
                "review": review,
                "sentiment": sentiment
            })

        return jsonify(result)

    except Exception as e:
        print("SEARCH ERROR:", e)
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route("/reviews")
def reviews():
    return jsonify(get_reviews())


if __name__ == "__main__":
    app.run(debug=True)