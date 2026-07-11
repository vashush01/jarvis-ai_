from openai import OpenAI

client = OpenAI(
    api_key="your_api"
)
completion = client.chat.completions.create(
    model ="gpt-3.5-turbo",
         messages=[
            {"role": "system", "content": "You are a virtual assistant."},
            {"role": "user", "content": "Who is Virat Kohli"}
        ],
)
print(completion.choices[0].message)