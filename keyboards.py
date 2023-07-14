from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    InlineKeyboardButton, InlineKeyboardMarkup

Economy, War, Politics = KeyboardButton("Экономика💹"), KeyboardButton("Война⚔"), KeyboardButton("Механики⚙")
Resurs, Treasur, Army = KeyboardButton("Ресурсы⛏"), KeyboardButton('Печать денег🪙'), KeyboardButton("Армия🛡")
info = KeyboardButton('Информация об экономикеℹ')
back = KeyboardButton('Назад🔙')
Next = KeyboardButton('Следующий день⏭')
Factory, oil = KeyboardButton('Построить гражданcкие фабрики🛠'), KeyboardButton(
    'Построить нефтебазу⚒')
procent_1, procent_2_5, procent_5, procent_10, procent_25 = KeyboardButton('1%😀'), KeyboardButton(
    '2.5%🙂'), KeyboardButton('5%😐'), KeyboardButton('10%🥲'), KeyboardButton('25%😬')
conscription, kit = KeyboardButton('Выбрать призыв🫡'), KeyboardButton('закупить снаряжение🧰')
war_Kafuron = KeyboardButton('Захватить Kafuron')
war_Klalkriya = KeyboardButton('Захватить Klalkriya')
war_Keliktaniya = KeyboardButton('Захватить Keliktaniya')
choose_action = ReplyKeyboardMarkup(
    resize_keyboard=True).insert(Economy).insert(War).insert(Politics).insert(Next).insert(info)
choose_politic = ReplyKeyboardMarkup(
    resize_keyboard=True).insert(Resurs).insert(Treasur).insert(Army).insert(back)
info_button = ReplyKeyboardMarkup(resize_keyboard=True).insert(info)
choose_factory = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).insert(Factory).insert(oil).insert(
    back)
choose_army = ReplyKeyboardMarkup(resize_keyboard=True).insert(conscription).insert(kit).insert(back)
call = ReplyKeyboardMarkup(resize_keyboard=True).insert(procent_1).insert(procent_2_5).insert(procent_5).insert(
    procent_10).insert(procent_25).insert(back)
choose_war = ReplyKeyboardMarkup(resize_keyboard=True).insert(war_Klalkriya).insert(war_Keliktaniya).insert(
    war_Kafuron).insert(back)
before = ReplyKeyboardMarkup(resize_keyboard=True).insert(back)
