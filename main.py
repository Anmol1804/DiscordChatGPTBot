import os
import discord
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.environ['SECRET_KEY']


class MyClient(discord.Client):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')

    if self.user != message.author:
      if self.user in message.mentions:

        channel = message.channel

        response = openai.Completion.create(model="gpt-3.5-turbo-instruct",
                                            prompt="",
                                            temperature=1,
                                            max_tokens=256,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0)
        messageToSend = response.choices[0].text
        await channel.send(messageToSend)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
