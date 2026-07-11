from openai import OpenAI

client = OpenAI(
    api_key="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"
)
completion = client.chat.completions.create(
    model ="gpt-3.5-turbo",
         messages=[
            {"role": "system", "content": "You are a virtual assistant."},
            {"role": "user", "content": "Who is Virat Kohli"}
        ],
)
print(completion.choices[0].message)