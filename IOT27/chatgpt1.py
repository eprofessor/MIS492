# this version writes out error messages to web page
# once get it running, also send entire message stream to web page
# PgP 3/27/2024

from openai import OpenAI

def main():
    f = open('/media/pi/MYDATA/chatGPT_API/chatgpt.txt', 'r')
    line1 = f.readline()  # read the chatGPT API key
    line1 = line1.strip()  # remove trailing and leading spaces
    f.close()

    client = OpenAI(api_key=line1)

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant"
        }
    ]

    while True:
        try:
            message = input("You: ")

            messages.append(
                {
                    "role": "user",
                    "content": message
                }
            )

            chat = client.chat.completions.create(
                messages=messages,
                model="gpt-3.5-turbo"
            )

            reply = chat.choices[0].message
            cpage(message)

            print("Assistant: ", reply.content)

            messages.append(reply)
            cpage(message)
        except Exception as e:
            print("An error occurred:", e)
            cpage(e)

def cpage(message):
    with open("/var/www/html/cgpt.html", "w") as html_file:
        html_file.write("<meta http-equiv='refresh' content='300'>")
        html_file.write("<html><head><title>chat GPT</title></head><body>")
        html_file.write("<h1>my AI conversations</h1>")
        html_file.write("<p> I asked: </p>")
        html_file.write("<p> chatGPT replied: {} </p>".format(message))
        html_file.write("</body></html>")

    print("HTML file created: cgpt.html")

if __name__ == "__main__":
    main()
