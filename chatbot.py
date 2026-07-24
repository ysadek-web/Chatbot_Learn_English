from dotenv import load_dotenv
from openai import OpenAI

from config import MODEL, TEMPERATURE, MAX_OUTPUT_TOKENS, SYSTEM_PROMPT

load_dotenv()

def get_response(messages):
    client = OpenAI()
    response = client.responses.create(
        model=MODEL,
        instructions=SYSTEM_PROMPT,
        input=messages, 
        temperature=TEMPERATURE,
        max_output_tokens=MAX_OUTPUT_TOKENS
    )
    return response.output_text
