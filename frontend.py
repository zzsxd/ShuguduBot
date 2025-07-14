from telebot import types


class Bot_inline_btns:
    def __init__(self):
        super(Bot_inline_btns, self).__init__()
        self.__markup = types.InlineKeyboardMarkup(row_width=1)

    def start_buttons(self):
        one = types.InlineKeyboardButton('💫 Подписаться на канал', url="https://t.me/ShuGuDuLashes")
        two = types.InlineKeyboardButton('📞 Поделиться номером', callback_data="share_contact")
        self.__markup.add(one, two)
        return self.__markup
    
    def share_contact(self):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        one = types.KeyboardButton('📞 Отправить мой номер', request_contact=True)
        keyboard.add(one)
        return keyboard
    
    def tg_channel(self):
        one = types.InlineKeyboardButton('Подписаться на канал', url="https://t.me/ShuGuDuLashes")
        self.__markup.add(one)
        return self.__markup
    
    def im_subscribe(self):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        one = types.KeyboardButton('💫 Я подписан!')
        keyboard.add(one)
        return keyboard
    
    def admin_buttons(self):
        one = types.InlineKeyboardButton('🔹 Экспорировать', callback_data="export_users")
        self.__markup.add(one)
        return self.__markup
    
    def support_buttons(self):
        one = types.InlineKeyboardButton("📞 Служба поддержки", url="https://taplink.cc/shugudusupport")
        self.__markup.add(one)
        return self.__markup