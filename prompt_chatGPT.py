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
OPTGPTINPUTPATH = '/Users/brianbarry/Desktop/computing/brian_utils/chatgptimput.md'

def submit_prompt(prompt: str) -> str:
    print(f'\n\n\n\n {prompt} \n\n\n\n')
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

        if prompt == ('md'):
            print('Okay! ;) Using an .md file as input')
            with open(OPTGPTINPUTPATH, 'r') as f:
                prompt = f.read()
            submit_prompt(prompt)
        ans = submit_prompt(prompt)
        print(ans)