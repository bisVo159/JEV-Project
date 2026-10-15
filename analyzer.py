import os
from dotenv import load_dotenv
from questions import QUESTIONS, TOPICS
from typesafe_sdk import TypeSafeClient

load_dotenv()

client = TypeSafeClient(
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api",
)

MENTION_THRESHOLD = 0.5

def analyze_review(review_text):
    """
    Analyzes a single review text and returns a dictionary of ratings for each topic.
    If a topic is not mentioned, it will not be included in the returned dictionary.
    """
    result = client.system_one(
        model="jev-1.13",
        state=review_text,
        questions=QUESTIONS
    )

    ratings = {}
    for topic_name,topic_id in TOPICS.items():  
        if result.answers.get(f"{topic_id}_mentioned").noul>=MENTION_THRESHOLD:
            rating_value = result.answers[f"{topic_id}_rating"].score
            ratings[topic_name] = rating_value

    return ratings
