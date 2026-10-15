import os
from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient

load_dotenv()

client = TypeSafeClient(
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api",
)

result = client.system_one(
    model="jev-1.13",
    state="I was charged twice for my subscription.",
    questions={
        "refund": {"type": "noul", "instructions": "Is the customer asking for money back?"},
        "department": {
            "type": "choice",
            "instructions": "Which team should handle this?",
            "criteria": {"billing": "Charges and refunds", "technical": "Bugs and outages"},
        },
    },
)

print(result.answers)