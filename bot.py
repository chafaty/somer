import telebot
bot = telebot.TeleBot("7027117590:AAE_HwevALZYCh4OYfoHOrqk_Vk6hUv2COs")
                                  
S = '''@YQQOQ
Run Bot . . . . .
'''
##
ALasmSomra = {
'آ': '𐎀',
    'إ': '𐎀',
    'أ': '𐎀',
    'ء': '𐎀',
    'ٱ': '𐎀',
    'گ': '𐎋',
     ' ':' ',
    'كَ': '𐎋',
    'ڪ': '𐎋',
    'ض': '𐎑',
    'ئ': '𐎛',
    'ێ': '𐎛',
    'ىٰ': '𐎛',
    'چ': '𐎂',
    'ﺟ': '𐎂',
    'ة': '𐎅',
    'ض': '𐎑',
    'ﺧ': '𐎃',
    'ﺣ': '𐎈',
    'ࢪ': '𐎗',
    'ه‍': '𐎅',
    'ﻏ': '𐎙',
    'ﻐ': '𐎙',
    'ﻤ': '𐎎',
    'ڤ': '𐎔',
    'טּ': '𐎐',
    'ﻧ': '𐎐',
    'ﯾ ': '𐎊',
    'ﻲ': '𐎊',
    'נ': '𐎄',
   'ﻈ': '𐎑',
    'ژ': '𐎇',
    'ا': '𐎀',
    'ب': '𐎁',
    'ج': '𐎂',
    'خ': '𐎃',
    'د': '𐎄',
    'ه': '𐎅',
    'و': '𐎆',
    'ز': '𐎇',
    'ح': '𐎈',
    'ط': '𐎉',
    'ي': '𐎊',
    'ك': '𐎋',
    'ش': '𐎌',
    'ل': '𐎍',
  'لّٰ': '𐎍',
    'م': '𐎎',
    'ذ': '𐎏',
    'ن': '𐎐',
    'ظ': '𐎑',
    'س': '𐎒',
    'ع': '𐎓',
    'ف': '𐎔',
    'ص': '𐎕',
    'ق': '𐎖',
    'ر': '𐎗',
    'ث': '𐎘',
    'غ': '𐎙',
    'ㅤ': 'ㅤ',
    '؏': '𐎓',
    'ت': '𐎚',
    'ى': '𐎛',
    'ؤ': '𐎜',
    'ڛ': '𐎝'
}
##
@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.reply_to(message, '''اهلاً بك في بوت تحويل الاسم الى اللغة السومرية  🇮🇶. 
ارسل اسمك الان باللغة العربية فقط 📍.
[❲ المطور ❳](YQQOQ.t.me)''',parse_mode="markdown")

@bot.message_handler(func=lambda message: True)
def SOMRE(message):
    Name = message.text
    SOMRE = ''

    if Name.isalpha():
        for char in Name:
            if char in ALasmSomra:
                SOMRE += ALasmSomra[char]
            else:
                SOMRE += char
        
        bot.reply_to(message, f'''الاسم الذي ارسلتة 🤏 :  {Name}
الاسم باللغة السومرية 🇮🇶 :`{SOMRE}`


📍|| للنسخ اضغط على الاسم للنسخ 💥. ''',parse_mode="markdown")

    else:
        bot.reply_to(message, 'ارسل اسمك باللغة العربية فقط 🫀.')
print(S)
bot.infinity_polling()
