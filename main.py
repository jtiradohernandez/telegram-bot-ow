import telebot
import random
import discord
import os
from discord import voice_state
from telebot import types

#Conection with our bot
TOKEN = os.getenv('TOKEN')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHATID= os.getenv('CHATID')
bot = telebot.TeleBot(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

discordClient = discord.Client(intents=intents)

#Images of memes
img_url = list()
img_url.append('https://static1.cbrimages.com/wordpress/wp-content/uploads/2018/01/Zarya-Overwatch-Meme.jpg')
img_url.append('https://i.chzbgr.com/full/9704497920/hABB5E0AB')
img_url.append('https://i.chzbgr.com/full/9704499456/h36B7B747')
img_url.append('https://i.pinimg.com/originals/27/74/b1/2774b10ac78dd8088bcaf69924eb9d6a.jpg')
img_url.append('https://cdn.memes.com/up/24609451572729529/vt/1572730824566.jpg')
img_url.append('https://i1.sndcdn.com/artworks-000200979003-auhijw-t500x500.jpg')
img_url.append('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpuyjCI8vmEjR7_OAPSE3vermbVZaZDhDNPsXOEsx94mtcBgdY1LRiJ_BLpMaFTK1EJoE&usqp=CAU')
img_url.append('https://preview.redd.it/what-if-we-could-change-the-music-that-lucio-played-like-we-v0-867xufhsn2ga1.png?auto=webp&s=997e100164883b64dfd4e19e3151d5e03e971a07')
img_url.append('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEImXRSA-Cjppn192pdVPgpTZ7m2zVqosUqQ&usqp=CAU')
img_url.append('https://i.ytimg.com/vi/PC_D1NSC-VU/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLD4Q3RMM8n2gAeaJ8ifvKbqo5SsLg')
img_url.append('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8ffio80xz7aO_-nTkEJF1gXv_GPkOzPpH4mwn8iJbjZyVX0UW_KA9gQkmV2vy6NOvDTA&usqp=CAU')
img_url.append('https://pm1.aminoapps.com/6521/bf341d25011c676a1d595bf820b1f85253829013_hq.jpg')
img_url.append('https://i.imgflip.com/1iq6x2.jpg')
img_url.append('https://img.wattpad.com/7df3626e66c6b681e5fe6dc067847f225ed4c341/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f662d5a617348366a784745484d413d3d2d3838392e313461396365386538313765376135353738323231353137323334342e676966')
img_url.append('https://i.pinimg.com/originals/52/da/54/52da5456c13e9240159234c1d07503d6.jpg')
img_url.append('https://i.imgflip.com/1w2q1x.jpg')
img_url.append('https://i.kym-cdn.com/photos/images/original/001/118/117/f07.png')
img_url.append('https://i.pinimg.com/originals/7a/c9/67/7ac967cc56b63159ba7d66ffc461c116.png')
img_url.append('https://scontent.fbcn12-1.fna.fbcdn.net/v/t31.18172-8/29351836_604467429910648_7595459686276065140_o.png?_nc_cat=109&ccb=1-7&_nc_sid=13d280&_nc_ohc=9MxjbGXVXqYQ7kNvgFmUKmq&_nc_ht=scontent.fbcn12-1.fna&oh=00_AYC-ZqFF5EHo1AcHc7-Lwow5rv56ipUH2C3Ra-NnMx-JNg&oe=66DC3984')

#Basic commands
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Bienvenido! Soy el bot que has creado para el canal de los nabos que juegan al overwatch')

@bot.message_handler(commands=['help'])
def send_help():
    bot.reply_backend('Puedes usar los siguientes comandos: 1. /start  2./help  3./meme')

#Customcommands
@bot.message_handler(commands=['meme'])
def send_meme(message):
    random_img = random.choice(img_url)
    bot.send_photo(chat_id=message.chat.id,photo = random_img)

#No command found
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, 'Este comando no existe')

#Send notification when user is online
@discordClient.event
async def on_voice_state_update(member, before, after):
    if after.channel.name == 'Overwatch':
        match member.name:
            case "dakuxavi":
                bot.send_message(chat_id=CHATID, text = "Xavi está jugando a Overwatch")
            case "monica211989":
                bot.send_message(chat_id=CHATID, text = "Mónica está jugando a Overwatch")
            case "_irlanda":
                bot.send_message(chat_id=CHATID, text = "Ricard está jugando a Overwatch")
            case "darklesc.":
                bot.send_message(chat_id=CHATID, text = "Juan Carlos está jugando a Overwatch")
            case "comolainfusion":
                bot.send_message(chat_id=CHATID, text = "Thais está jugando a Overwatch")
            case "gunnergrinch":
                bot.send_message(chat_id=CHATID, text = "Carlos está jugando a Overwatch")
            case "victor756":
                bot.send_message(chat_id=CHATID, text = "Victor no está jugando a Overwatch, pero se ha conectado")
            case _:
                bot.send_message(chat_id=CHATID, text = "Un desconocido ha entrado al canal de Overwatch")

discordClient.run(DISCORD_TOKEN)

if __name__ == "__main__":
     bot.polling(none_stop=True)


