from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def admin_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("➕ Kitob qo'shish"),
        KeyboardButton("📚 Kitoblar"),
        KeyboardButton("ℹ️ Kitobga ma'lumot qo'shish")
    )
    return markup

#Tugmalarni bittada qo'shib kettim bir yola ustoz