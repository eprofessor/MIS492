#PgP 2/10/2024 chatGPT API call from PiMyLifeUp article
# https://pimylifeup.com/raspberry-pi-chatgpt/
# modified to add USB flash drive to contain chatGPT API key
# need to have billing setup to get this to run

from openai import OpenAI

# 
# USB flash drive must be named "MYDATA"
# make sure chatgpt.txt file is on USB flashdrive plugged into RPi
# chatgpt.txt must contain chatGPT API key on line 1 and NOTHING else
#

f = open('/media/pi/MYDATA/chatgpt.txt', 'r')
line1=f.readline() # read the chatGPT API key
line1=line1.strip()  #remove trailing and leading spaces

print('chatGPT API key: ', line1)   #echo key

client = OpenAI(
    api_key=line1
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant"
    }
]

while True:
    message = input("You: ")

    messages.append(
        {
            "role": "user",
            "content": message
        },
    )

    chat = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo"
    )

    reply = chat.choices[0].message

    print("Assistant: ", reply.content)
    
    messages.append(reply)