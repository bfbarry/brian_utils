from openai import OpenAI
import os
from typing import List
from dotenv import load_dotenv
import json

MODEL = "gpt-4o"
load_dotenv()
HERE_DIR = os.path.dirname(__file__)
CLIENT = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

def submit_prompt(prompt: str) -> str:
    res = CLIENT.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are ChatGPT, a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
    return res.choices[0].message.content


if __name__ == '__main__':
    print(f'Welcome to {MODEL}')
    while 1:
        prompt = input('>> ')
        print('...')
        ans = submit_prompt(prompt)
        print(ans)