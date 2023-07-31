import os
import sys


import openai


#   https://wooiljeong.github.io/python/chatgpt-api/
if __name__ == '__main__':
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    if openai_api_key is None or 0 == len(openai_api_key):
        sys.exit(1)
    print(openai_api_key)

    openai.api_key = openai_api_key
    model = "gpt-3.5-turbo"

    messages = [
        {"role": "system", "content": "You are a helpful assistant such as client support via phone call. Working in the 하나더 telecom company. Act very calm & kindly"},
        {"role": "user", "content": "I will speak like a mad customer because I didn't get the phone case distributed in the previous week's event"}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    answer = response['choices'][0]['message']['content']
    print(answer)

    query = '아니 사람들이 여기서 공짜로 핸드폰 케이스 받았다는데 저는 못 받았어요. 저는 왜 안줘요?'

    messages = [
        {"role": "system", "content": "React as described, reply in Korean"},
        {"role": "user", "content": query}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    answer = response['choices'][0]['message']['content']
    print(answer)
