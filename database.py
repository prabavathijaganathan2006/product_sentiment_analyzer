reviews_data = []

def save_review(review, sentiment):
    reviews_data.append({
        "review": review,
        "sentiment": sentiment
    })

def get_reviews():
    return reviews_data