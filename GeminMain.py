from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
import os

api_key = os.environ.get("GOOGLE_API_KEY")

if api_key is None:
    raise ValueError("The API key is not set. Please set the GOOGLE_API_KEY environment variable.")

client = genai.Client(api_key=api_key)

model_id = "gemini-2.0-flash-exp"

google_search_tool = Tool(
    google_search = GoogleSearch()
)

response = client.models.generate_content(
    model=model_id,
    contents="who are you?",
    config=GenerateContentConfig(
        tools=[google_search_tool],
        response_modalities=["TEXT"],
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# Example response:
# The next total solar eclipse visible in the contiguous United States will be on ...

# To get grounding metadata as web content.
# print(response.candidates[0].grounding_metadata.search_entry_point.rendered_content)