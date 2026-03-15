import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_recommendation(resource_data):
    """
    Generate AI recommendation for AWS cost optimization
    """

    prompt = f"""
    You are a senior DevOps cloud cost optimization expert.

    Analyze the following AWS resource data and give a recommendation
    to reduce cost.

    Resource details:
    {resource_data}

    Provide:
    1. Problem
    2. Recommendation
    3. Estimated cost impact
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a DevOps cloud optimization assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content