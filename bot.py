from pyrogram import Client, filters

from pyrogram.types import  InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

import os 

TOKEN = os.environ.get("TOKEN","")
API_ID =int(os.environ.get("API_ID",12345))
API_HASH =os.environ.get("API_HASH","")


app= Client("Thumbot",bot_token=TOKEN,api_hash=API_HASH,
            api_id=API_ID)

@app.on_message(filters.command(['start']))
def start(client, message):
            message.reply_text(text =f"Hello {message.from_user.first_name } \n\n **I am simple YouTube Thumbnail link Generator** \n __Send me Youtube link and get Thumbnail link__",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/DOSTI_GROUP_1234") ],
                 [InlineKeyboardButton("Channel 🧐", url="https://t.me/abhinasroy") ]
           ]
        ) )


@app.on_message(filters.regex("^https?:\/\/?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/).{11}"))
def gyt(client,message):
	
	try:
		ms = message.reply_text("```checking valid link or not ```",reply_to_message_id = message.message_id )
		url =message.matches[0].group(0)
		video = YouTube(url)
		thumb = video.thumbnail_url
		app.send_photo(message.chat.id ,photo = thumb, reply_markup=InlineKeyboardMarkup([    [ InlineKeyboardButton("🔗 link" ,url=thumb) ]]))
		ms.delete()
        
	except VideoUnavailable:
		ms.edit("**Invalid video link!**")


		


app.run()
	
