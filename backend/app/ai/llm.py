# simple LLM wrapper around OpenAI
import os
import openai

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def ask(prompt: str):
    if not OPENAI_API_KEY:
        return "OpenAI API key not configured"
    resp = openai.ChatCompletion.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return resp.choices[0].message.content
