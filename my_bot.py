from __future__ import annotations

from config import Token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from keyboards import *
from bot_text import *

bot = Bot(Token)
dp = Dispatcher(bot, storage=MemoryStorage())
storage = MemoryStorage()


def print_data(my_dict):
    economy_status = (parametrs[0] + str(my_dict["date"]) + '\n \n' + parametrs[1] + '\n' + parametrs[2] +
                      str(my_dict['population']) + '\n' + parametrs[3] + str(my_dict['pop_growth']) + '\n \n' +
                      parametrs[4] + '\n' + parametrs[5] + str(my_dict['sold']) + '\n' + parametrs[6] +
                      str(my_dict['ready_cons']) + '\n' + parametrs[7] + str(my_dict['cons']) + '\n' +
                      parametrs[8] + str(my_dict['cons_per']) + '\n' + parametrs[9] + str(my_dict['outfit']) +
                      '\n' + parametrs[10] + str(my_dict['outfit_cost']) + '\n \n' + parametrs[11] + '\n' +
                      parametrs[12] + str(my_dict['money']) + '\n' + parametrs[13] + str(my_dict['min_money']) + '\n' +
                      parametrs[14] + str(my_dict['money_cost']) + '\n' + parametrs[15] + str(my_dict['more_money'])
                      + '\n' + parametrs[16] + str(my_dict['fuel']) + '\n' + parametrs[17] +
                      str(my_dict['fuel_factory']) + '\n' + parametrs[18] + str(my_dict['fuel_produce']) + '\n' +
                      parametrs[19] + str(my_dict['fuel_cost']) + '\n' + parametrs[20] + str(my_dict['products']) +
                      '\n' + parametrs[21] + str(my_dict['products_factory']) + '\n' + parametrs[22] +
                      str(my_dict['products_produce']) + '\n' + parametrs[23] + str(my_dict['products_cost']))
    return economy_status


@dp.message_handler(commands='start', state='*')
async def start_handler(message: types.Message, state):
    await state.update_data(date=1,
                            population=100000, pop_growth=1.1,
                            sold=100, ready_cons=5, cons=20, cons_per=0.01, outfit=8000, outfit_cost=5,
                            money=10000, min_money=501250, money_cost=1, more_money=0, fuel=10000, fuel_factory=10,
                            fuel_produce=100000, fuel_cost=3, products=150000, products_factory=20,
                            products_produce=200000, products_cost=3,
                            Kafuron_f_fact=100, Kafuron_w=0, Kafuron_p_fact=100, Kafuron_m=100000, Klalkriya_f_fact=70,
                            Klalkriya_p_fact=60, Klalkriya_m=50000, Klalkriya_w=0, Keliktaniya_f_fact=20,
                            Keliktaniya_p_fact=10, Keliktaniya_m=10000, Keliktaniya_w=0, w=0, f=0, population_b=100000)
    with open('images/ancient_text.jpg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer(introduction, reply_markup=info_button)
    with open('images/worldmap (1).jpg', 'rb') as img:
        await message.answer_photo(img)
    await state.set_state('1')


@dp.message_handler(state='1')
async def status(message, state):
    data = await state.get_data()
    await message.answer(print_data(data), reply_markup=choose_action)
    await state.set_state('Меню')


@dp.message_handler(state='Меню')
async def menu(message, state):
    if message.text == 'Механики⚙':
        await state.set_state('Механика')
        await mehanic(message, state)
    elif message.text == 'Экономика💹':
        await state.set_state('Экономика')
        await economic(message, state)
    elif message.text == 'Война⚔':
        await state.set_state('Войны')
        await war(message, state)
    elif message.text == 'Следующий день⏭':
        data = await state.get_data()
        await state.update_data(date=data['date'] + 1)  # изменение даты
        data = await state.get_data()
        if data['date'] % 3 == 0:
            if data['outfit'] >= data['ready_cons']:
                await state.update_data(outfit=data['outfit'] - data['ready_cons'])
                data = await state.get_data()
                await state.update_data(sold=data['sold'] + data['ready_cons'])  # изменение солдат + снаряжения
                data = await state.get_data()
                await state.update_data(ready_cons=0)
                data = await state.get_data()
            else:
                await state.update_data(sold=data['outfit'])
                data = await state.get_data()
                await state.update_data(ready_cons=data['ready_cons'] - data['outfit'])
                await state.update_data(outfit=0)
        if data['date'] % 7 == 0:
            await state.update_data(ready_cons=data['ready_cons'] + data['cons'])
            data = await state.get_data()
            await state.update_data(cons=0)
        await state.update_data(population_b=data['population'])
        data = await state.get_data()
        if data['date'] % 10 == 0:
            if ((data['cons'] + data['ready_cons'] + data['sold']) / data['population']) < data['cons_per']:
                await state.update_data(cons=data['cons'] + data['population'] * (
                        data['cons_per'] - (data['sold'] + data['ready_cons'] + data['cons']) / data['population']))
                data = await state.get_data()
            await state.update_data(population=(data['population'] * data['pop_growth']) - (data['population'] * (
                    data['cons_per'] - (data['sold'] + data['cons'] + data['ready_cons']) / data['population'])))
        # изменение мирного населения
        data = await state.get_data()
        await state.update_data(money_cost=data['min_money'] / (data['money'] + data['more_money']))
        data = await state.get_data()
        await state.update_data(money=data['money'] + (data['population'] * ((1 / data['money_cost']) / 20)) - (
            # изменение общего количества денег
                data['sold'] + data['cons'] + data['ready_cons']) * (4 / data['money_cost']))
        data = await state.get_data()
        await state.update_data(
            products_produce=data['products_factory'] * 10000 - (data['sold'] + data['cons'] +  # производство продуктов
                                                                 data['ready_cons']) - 2 * data['population'])
        data = await state.get_data()
        await state.update_data(products=data['products'] + data['products_produce'])  # продукты на складах
        data = await state.get_data()
        data = await state.get_data()
        await state.update_data(
            fuel_produce=data['fuel_factory'] * 10000 - 4 * (data['sold'] + data['cons'] +  # производство нефти
                                                             data['ready_cons']) - data['population'])
        data = await state.get_data()
        await state.update_data(fuel=data['fuel'] + data['fuel_produce'])  # нефть на складах
        data = await state.get_data()
        if data['fuel_produce'] < 0:
            if data['fuel'] / data['fuel_produce'] >= 60:
                data = await state.get_data()
                await state.update_data(fuel_cost=5 / data['money_cost'])
            else:
                data = await state.get_data()
                await state.update_data(fuel_cost=6 / data['money_cost'])
        elif data['fuel_produce'] == 0:
            data = await state.get_data()
            await state.update_data(fuel_cost=4 / data['self.money_cost'])
        else:
            if (data['fuel_produce'] / (
                    2 * (data['sold'] + data['cons'] + data['ready_cons']) + 1 * data['population'])) >= 2:
                data = await state.get_data()
                await state.update_data(fuel_cost=2 / data['money_cost'])
            else:
                data = await state.get_data()
                await state.update_data(fuel_cost=3 / data['money_cost'])  # зменение стоимости топлива
        if data['products_produce'] < 0:
            if data['products'] / data['products_produce'] >= 60:
                data = await state.get_data()
                await state.update_data(products_cost=4 / data['money_cost'])
            else:
                data = await state.get_data()
                await state.update_data(products_cost=3 / data['money_cost'])
        elif data['products_produce'] == 0:
            data = await state.get_data()
            await state.update_data(products_cost=2 / data['self.money_cost'])
        else:
            if (data['products_produce'] / (
                    data['sold'] + data['cons'] + data['ready_cons'] + 2 * data['population'])) >= 2:
                data = await state.get_data()
                await state.update_data(products_cost=1 / data['money_cost'])
            else:
                data = await state.get_data()
                await state.update_data(products_cost=2 / data['money_cost'])  # зменение стоимости продуктов
        data = await state.get_data()
        await state.update_data(
            pop_growth=1.1 + data['money_cost'] * 0.01 - (data['fuel_cost'] + data['products_cost']) * 0.01)
        data = await state.get_data()
        data = await state.get_data()
        await state.set_state('1')
        data = await state.get_data()
        await state.update_data(min_money=(data['population'] * 5 / data['money_cost']) + (10 / data['money_cost']) * (
                    data['sold'] + data['cons'] + data['ready_cons']))
        await status(message, state)
        data = await state.get_data()
        await state.update_data(Kafuron_f_fact=data['Kafuron_f_fact'] + 0.1)
        data = await state.get_data()
        await state.update_data(Kafuron_p_fact=data['Kafuron_p_fact'] + 0.1)
        data = await state.get_data()
        await state.update_data(Kafuron_m=data['Kafuron_m'] + 20)
        data = await state.get_data()
        await state.update_data(Klalkriya_f_fact=data['Klalkriya_f_fact'] + 0.1)
        data = await state.get_data()
        await state.update_data(Klalkriya_p_fact=data['Klalkriya_p_fact'] + 0.1)
        data = await state.get_data()
        await state.update_data(Klalkriya_m=data['Klalkriya_m'] + 10)
        data = await state.get_data()
        await state.update_data(Keliktaniya_f_fact=data['Keliktaniya_f_fact'] + 0.1)
        data = await state.get_data()
        await state.update_data(Keliktaniya_p_fact=data['Keliktaniya_p_fact'] + 0.1)
        data = await state.get_data()
        await state.update_data(Keliktaniya_m=data['Keliktaniya_m'] + 3)
        if data['products'] <= 0:
            await message.answer('Ваши подданные умерли от голода, вы не смогли возродить империю',
                                 reply_markup=ReplyKeyboardRemove())
        if data['fuel'] <= 0:
            await message.answer('Ваша промышленность рухнула по причине нехватки топлива, вы проиграли',
                                 reply_markup=ReplyKeyboardRemove())
        if data['money'] <= 0:
            await message.answer('Ваша экономика не выдержала такой экономической нагрузки, вы проиграли.',
                                 reply_markup=ReplyKeyboardRemove())
        if data['Kafuron_w'] == data['Kafuron_w'] == data['Kafuron_w'] == 2:
            await message.answer('Вы смогли происоединить к себе все земли империи. ПОБЕДА!!!',
                                 reply_markup=ReplyKeyboardRemove())

    elif message.text == 'Информация об экономикеℹ':
        data = await state.get_data()
        await message.answer(print_data(data), reply_markup=choose_action)
        await state.set_state('Меню')


@dp.message_handler(state='Экономика')
async def economic(message: types.Message, state: FSMContext):
    await message.answer('Вы находитесь во вкладке экономика', reply_markup=choose_politic)
    await state.set_state('Выбор_экономики')


@dp.message_handler(state='Выбор_экономики')
async def chose_politic(message: types.Message, state: FSMContext):
    if message.text == 'Ресурсы⛏':
        await message.answer(
            'Здесь вы можете построить заводы по производству ресурсов, необходимых вам для мирных жителей и армии',
            reply_markup=choose_factory)
        await state.set_state('Выбор завода')
    elif message.text == 'Печать денег🪙':
        await state.set_state('Печать денег')
        await message.answer('введите сколько денег вы хотите напечатать', reply_markup=ReplyKeyboardRemove())
    if message.text == 'Армия🛡':
        await message.answer(
            'Здесь вы можете изменить уровень своего призыва и закупить снаряжение, необходимое для размещения армии',
            reply_markup=choose_army)
        await state.set_state('Выбор военной политики')
    elif message.text == 'Назад🔙':
        await message.answer('Вы вернулись на предыдущую вкладку', reply_markup=choose_action)
        await state.set_state('Меню')


@dp.message_handler(state='Выбор завода')
async def Factory(message: types.Message, state: FSMContext):
    if message.text == 'Построить гражданcкие фабрики🛠':
        await state.set_state('ТНП')
        await message.answer(
            'введите столько фабрик, сколько вы хотите построить. Цена фабрики - 5000 (Фабрики строятся мнгновенно)',
            reply_markup=ReplyKeyboardRemove())
    elif message.text == 'Построить нефтебазу⚒':
        await state.set_state('ТФ')
        await message.answer(
            'введите столько фабрик, сколько вы хотите построить. Цена фабрики : 10000 (Фабрики строятся мнгновенно)',
            reply_markup=ReplyKeyboardRemove())
    elif message.text == 'Назад🔙':
        await message.answer('Вы вернулись на предыдущую вкладку', reply_markup=choose_politic)
        await state.set_state('Выбор_экономики')


@dp.message_handler(state='Выбор военной политики')
async def Factory(message: types.Message, state: FSMContext):
    if message.text == 'закупить снаряжение🧰':
        await state.set_state('снаряжение')
        await message.answer(
            'введите сколько снаряжения вы хотите закупить',
            reply_markup=ReplyKeyboardRemove())
    elif message.text == 'Выбрать призыв🫡':
        await state.set_state('призыв')
        await message.answer('выберите процент процент призыва', reply_markup=call)
    elif message.text == 'Назад🔙':
        await message.answer('Вы вернулись на предыдущую вкладку', reply_markup=choose_politic)
        await state.set_state('Выбор_экономики')


@dp.message_handler(state='Печать денег')
async def print_money(message, state):
    data = await state.get_data()
    await state.update_data(money=data['money'] + int(message.text))
    data = await state.get_data()
    await state.update_data(more_money=int(message.text) + data['more_money'])
    data = await state.get_data()
    await state.update_data(money_cost=data['min_money'] / (data['money'] + data['more_money']))
    data = await state.get_data()
    await state.set_state('Экономика')
    await economic(message, state)


@dp.message_handler(state='ТНП')
async def build_TNP(message, state):
    data = await state.get_data()
    await state.update_data(products_factory=int(message.text) + data['products_factory'])
    data = await state.get_data()
    await state.update_data(money=data['money'] - 10000 * int(message.text))
    await state.set_state('ТНП')
    await economic(message, state)


@dp.message_handler(state='ТФ')
async def build_FF(message, state):
    data = await state.get_data()
    await state.update_data(fuel_factory=int(message.text) + data['fuel_factory'])
    data = await state.get_data()
    await state.update_data(money=data['money'] - 30000 * int(message.text))
    await state.set_state('ТФ')
    await economic(message, state)


@dp.message_handler(state='снаряжение')
async def buy_outfit(message, state):
    data = await state.get_data()
    if int(message.text) * data['outfit_cost'] / data['money_cost'] >= data['money']:
        await state.update_data(money=data['money'] - (data['outfit_cost'] / data['money_cost']) * (
                data['money'] // (data['outfit_cost'] / data['money_cost'])))
        data = await state.get_data()
        await state.update_data(outfit=data['outfit'] + data['money'] // (data['outfit_cost'] / data['money_cost']))
    else:
        await state.update_data(money=data['money'] - int(message.text) * (data['outfit_cost'] / data['money_cost']))
        data = await state.get_data()
        await state.update_data(outfit=data['outfit'] + int(message.text))
    await state.set_state('снаряжение')
    await economic(message, state)


@dp.message_handler(state='призыв')
async def another_outfit(message, state):
    data = await state.get_data()
    if message.text == 'Назад🔙':
        await message.answer('Вы вернулись на предыдущую вкладку', reply_markup=choose_army)
        await state.set_state('Выбор_экономики')
    elif message.text == '1%😀':
        await state.update_data(cons_per=0.01)
    elif message.text == '2.5%🙂':
        await state.update_data(cons_per=0.025)
    elif message.text == '5%😐':
        await state.update_data(cons_per=0.05)
    elif message.text == '10%🥲':
        await state.update_data(cons_per=0.1)
    elif message.text == '25%😬':
        await state.update_data(cons_per=0.25)
    await state.set_state('призыв')
    await economic(message, state)


@dp.message_handler(state='Войны')
async def war(message: types.Message, state: FSMContext):
    await message.answer('Вы находитесь во вкладке война', reply_markup=choose_war)
    await state.set_state('Объявить войну')


@dp.message_handler(state='Объявить войну')
async def war_c(message: types.Message, state: FSMContext):
    if message.text == 'Захватить Keliktaniya':
        data = await state.get_data()
        if data['w'] == 0 and data['Keliktaniya_w'] == 0:
            await state.update_data(Keliktaniya_w=1)
            await state.update_data(w=1)
            if data['sold'] * 1.5 >= data['Keliktaniya_m']:
                data = await state.get_data()
                await state.update_data(w=0)
                await state.update_data(Keliktaniya_w=2)
                await message.answer('Вы завоевали государство Keliktaniya', reply_markup=choose_war)
                data = await state.get_data()
                await state.update_data(sold=data['sold'] - data['Keliktaniya_m'] * 1.2)
                await state.set_state('Объявить войну')
            else:
                data = await state.get_data()
                await state.update_data(f=1)
                await message.answer('Государство Keliktaniya завоевало вас, вы не смогли возродить империю',
                                     reply_markup=ReplyKeyboardRemove())
                await state.set_state('Объявить войну')
        elif data['Keliktaniya_w'] == 2:
            await message.answer('Вы уже захватили это государство', reply_markup=choose_war)
        else:
            await message.answer('Вы уже ведёте войну!', reply_markup=choose_war)
            await state.set_state('Объявить войну')
    elif message.text == 'Захватить Kafuron':
        data = await state.get_data()
        if data['w'] == 0 and data['Kafuron_w'] == 0:
            await state.update_data(Kafuron_w=1)
            await state.update_data(w=1)
            if data['sold'] * 1.5 >= data['Kafuron_m']:
                data = await state.get_data()
                await state.update_data(w=0)
                await state.update_data(Kafuron_w=2)
                await message.answer('Вы завоевали государство Kafuron', reply_markup=choose_war)
                data = await state.get_data()
                await state.update_data(sold=data['sold'] - data['Kafuron_m'] * 1.2)
                await state.set_state('Объявить войну')
            else:
                data = await state.get_data()
                await state.update_data(f=1)
                await message.answer('Государство Kafuron завоевало вас, вы не смогли возродить империю',
                                     reply_markup=ReplyKeyboardRemove())
                await state.set_state('Объявить войну')
        elif data['Kafuron_w'] == 2:
            await message.answer('Вы уже захватили это государство', reply_markup=choose_war)
        else:
            await message.answer('Вы уже ведёте войну!', reply_markup=choose_war)
            await state.set_state('Объявить войну')
    elif message.text == 'Захватить Klalkriya':
        data = await state.get_data()
        if data['w'] == 0 and data['Klalkriya_w'] == 0:
            await state.update_data(Klalkriya_w=1)
            await state.update_data(w=1)
            if data['sold'] * 1.5 >= data['Klalkriya_m']:
                data = await state.get_data()
                await state.update_data(w=0)
                await state.update_data(Klalkriya_w=2)
                await state.update_data(products_factory=data['products_factory'] + data['Klalkriya_p_fact'] // 2)
                data = await state.get_data()
                await state.update_data(fuel_factory=data['fuel_factory'] + data['Klalkriya_f_fact'] // 2)
                await message.answer('Вы завоевали государство Klalkriya', reply_markup=choose_war)
                data = await state.get_data()
                await state.update_data(sold=data['sold'] - data['Klalkriya_m'] * 1.2)
                await state.set_state('Объявить войну')
            else:
                data = await state.get_data()
                await state.update_data(f=1)
                await message.answer('Государство Klalkriya завоевало вас, вы не смогли возродить империю',
                                     reply_markup=ReplyKeyboardRemove())
                await state.set_state('Объявить войну')
        elif data['Klalkriya_w'] == 2:
            await message.answer('Вы уже захватили это государство', reply_markup=choose_war)
        else:
            await message.answer('Вы уже ведёте войну!', reply_markup=choose_war)
            await state.set_state('Объявить войну')
    elif message.text == 'Назад🔙':
        await message.answer('Вы вернулись на предыдущую вкладку', reply_markup=choose_action)
        await state.set_state('Меню')


@dp.message_handler(state='Механика')
async def mehanic(message: types.Message, state: FSMContext):
    await message.answer(mehanics, reply_markup=before)
    if message.text == 'Назад🔙':
        await message.answer('Вы вернулись на предыдущую вкладку', reply_markup=choose_action)
        await state.set_state('Меню')


executor.start_polling(dp, skip_updates=True)
