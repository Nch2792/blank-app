from openai import OpenAI
import json

client = OpenAI(
    api_key = "NOT AN API KEY"
)

system_prompt = """
You are a wiki maintainer for a Minecraft themed wikipedia website. A user will
come to you requesting to see a certain wiki page. Based on their request,
generate and return a JSON response representing the wiki page with the following fields:

{
    "name": the name of the article,
    "history": the history of the location or object, or if it's a character, their backstory,
    "characteristics": notable features of the location or object, or if it's a character, their personality,
    "trivia": some fun facts
}

The wiki page must be informative, not short (at least 150 words), and be formal.
"""

def get_json_response(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return json.loads(response.choices[0].message.content)
