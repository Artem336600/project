@dp.message_handler(state='age')
async  def age_handler(message, state):
    await message.answer('Эта функция никогда не вызовется')

@dp.message_handler(commands=['start_group_chat'])
async def start_handler(message):
    await message.answer('Вы присоединились к групgовому чату.')
    sp = list()
    user_id = message.from_user.id
    sp.append(user_id)




@dp.message_handler(commands=['cat'])
async def photo(message):
    url = 'https://api.thecatapi.com/v1/images/search?limit=10'
    response = requests.get(url).json()
    cat = response[0]['url']

    await message.answer_photo(cat)




@dp.message_handler()
async def reply(message):
    if message.text != 'Пригожин':
        await message.answer(message.text)
    else:
        await message.answer('https://www.youtube.com/watch?v=DHAFLzFE11Y')


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message, state='*'):
    await message.answer('Привет, как тебя зовут?')
    await state.set_state('name')

@dp.message_handler(state='name')
async def name_handler(message, state):
    name = message.text
    await state.update_data({'name': name})
    await message.answer(f'{name}, добро пожаловать!')
    await message.answer('Сколько тебе лет?')
    await state.set_state('age')

@dp.message_handler(state='age')
async def age_handler(message, state):
    age = message.text
    await state.update_data({'age': age})
    await message.answer(f'{age} твой возраст')
    await state.set_state('echo')

@dp.message_handler(state='echo')
async def echo_handler(message, state):
    user_data = await state.get_data()
    await message.answer(f"{user_data['name']} сказал: {message.text}")
    await message.answer(f"{user_data['name']} умер в возрасте {user_data['age']}")

@dp.message_handler(commands=['start'], state='*')
async def start_handler(message, state='*'):
    await message.answer('Привет, как тебя зовут?')
    await state.set_state('name')


@dp.message_handler(state='name')
async def name_handler(message, state):
    name = message.text
    await state.update_data({'name': name})
    await message.answer(f'{name}, добро пожаловать!')
    await message.answer('Сколько тебе лет?')
    await state.set_state('age')

@dp.message_handler(state='age')
async def age_handler(message, state):
    age = message.text
    await state.update_data({'age': age})
    await message.answer(f'{age} твой возраст')
    await state.set_state('echo')

@dp.message_handler(state='echo')
async def echo_handler(message, state):
    user_data = await state.get_data()
    await message.answer(f"{user_data['name']} сказал: {message.text}")
    await message.answer(f"{user_data['name']} умер в возрасте {user_data['age']}")




waiting_users: set[int] = set()
connected_pairs: dict[int, int] = {}
sp = []


@dp.message_handler(commands='start', state='*')
async def start_handler(message, state):
    await message.answer('Привет! Ты запустил викторину: Какой Пригожин ты сегодня?')
    name = message.text
    await message.answer('Как тебя зовут?')
    await state.update_data({'name': name})
    await state.set_state('1')


@dp.message_handler(state='1')
async def start_handler(message, state):
    await message.reply('Вопрос 1: Ты носишь бороду?', reply_markup=choose_chat_type_keyboard_1)
    await state.set_state('2')


@dp.message_handler(state='2')
async def start_handler(message, state):
    global sp
    sp.append(message.text)
    await message.answer('Вопрос 2: Ты лысый?', reply_markup=choose_chat_type_keyboard)
    await state.set_state('3')


@dp.message_handler(state='3')
async def start_handler(message, state):
    global sp
    sp.append(message.text)
    await message.answer('Вопрос 3: Ты носишь головной убор?', reply_markup=choose_chat_type_keyboard)
    await state.set_state('4')


@dp.message_handler(state='4')
async def start_handler(message, state):
    global sp
    sp.append(message.text)
    await message.answer('Вопрос 4: У тебя длинная борода?', reply_markup=choose_chat_type_keyboard)
    await state.set_state('5')

@dp.message_handler(state='5')
async def start_handler(message, state):
    global sp
    sp.append(message.text)
    await message.answer('Вопрос 5: Твоя шапка чёрная?', reply_markup=choose_chat_type_keyboard)
    await state.set_state('final')

@dp.message_handler(state='6')
async def start_handler(message, state):
    global sp
    sp.append(message.text)
    await message.answer('Вопрос 6: Ты умеешь улыбаться?', reply_markup=choose_chat_type_keyboard)
    await state.set_state('final')

@dp.message_handler(state='final')
async def start_handler(message: types.Message, state):
    global sp
    sp.append(message.text)
    if sp[0] == 2:
        await message.answer('', reply_markup=ReplyKeyboardRemove())