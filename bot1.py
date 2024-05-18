import telebot
from telebot.types import InlineKeyboardButton as Btn , InlineKeyboardMarkup as Mak
import zipfile
from io import BytesIO as io

token = "5289963311:AAGz2iXqYQSzQEie-anQNtcbVx2Z7LbGKIc"  #Token
bot = telebot.TeleBot(token)
btn = Mak().add(Btn("قناتي",url="Crrazy_8.t.me"))
@bot.message_handler(commands=["start"])
def welcome(message):
	bot.reply_to(message,'مرحبا عزيزي انا هنا لمساعدتك في فك ضغط الملفات الZip فقط ارسل الملف..',reply_markup=btn)
@bot.message_handler(content_types=['document'])
def document(message):
    if message.document.file_name.endswith('.zip'):
    	file_info = bot.get_file(message.document.file_id)
    	dow = bot.download_file(file_info.file_path)
    	with zipfile.ZipFile(io(dow)) as zip_ref:
    	       for file in zip_ref.namelist():
    	           if not file.endswith('/'):
    	           	ext = zip_ref.extract(file)
    	           	with open(ext, 'rb') as filee:
    	           		bot.send_document(message.chat.id,filee)
    else:
    	bot.reply_to(message,"جب أن يكون الملف امتداده .zip")
    	pass
bot.infinity_polling()
