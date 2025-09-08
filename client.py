from openai import OpenAI

client = OpenAI(
  api_key=""
)
command = '''

'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person name shrish , he speaks hindi aswell as english. he is from india. he is also a coder . You analyze chat history and respond like shrish "},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)


