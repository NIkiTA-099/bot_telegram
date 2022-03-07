import telebot, wikipedia, re
from telebot import types
import config
bot = telebot.TeleBot("Ссылка на бот")
wikipedia.set_lang("ru")
def kvest(message):
    if message.text == "🏃 Квест":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Запустить")
        button2 = types.KeyboardButton("Выйти")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Нажми кнопку ЗАПУСТИТЬ, если желаешь пройти квест", reply_markup=markup)
    elif message.text == "Запустить":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1")
        button2 = types.KeyboardButton("2")
        button3 = types.KeyboardButton("3")
        back = types.KeyboardButton("Выйти")
        markup.add(button1, button2, button3,back)
        bot.send_message(message.chat.id, "Ну что начинаем")
        bot.send_message(message.chat.id, text="Работает сирена ...\nВы проснулись в заброшенном МРК, понимаете что вы находитесь в бункере. Перед вами три двери,\n1.ведёт вас на улицу к смертельно-опасному вирусу\n2.Тупик\n3.Ведёт на этаж выше\nПеред вами сложный выбор, время идёт", reply_markup=markup)

    elif message.text == "1":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Попробовать снова")
        back = types.KeyboardButton("Выйти")
        markup.add(button1,back)
        bot.send_message(message.chat.id, "Вы открываете дверь видя перед собой луч свет,вдыхаете ядовитые пары,которые передаются воздушно-капельным путём, вы умираете на улице, как и все жители планеты Земля", reply_markup=markup)

    elif message.text == "Попробовать снова":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1")
        button2 = types.KeyboardButton("2")
        button3 = types.KeyboardButton("3")
        back = types.KeyboardButton("Выйти")
        markup.add(button1, button2, button3, back)
        bot.send_message(message.chat.id,text="Работает сирена ...\nВы проснулись в заброшенном МГВРК, понимаете что вы находитесь в бункере. Перед вами три двери,\n1.ведёт вас на улицу к смертельно-опасному вирусу\n2.Тупик\n3.Ведёт на этаж выше\nПеред вами сложный выбор, время идёт",reply_markup=markup)
    elif message.text =="Выйти":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("🔍 Поиск в Wikipedia")
        button2 = types.KeyboardButton("📚 Документация")
        button3 = types.KeyboardButton("📕 Скачать книгу")
        button4 = types.KeyboardButton("🏃 Квест")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id,text="Вы вышли из квеста",reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Увы, я такое не умею")
def get_text_messages(message):
    if (message.text == "👋 Поздороваться"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        button3 = types.KeyboardButton("🆘HELP🆘")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Привеет, чем могу помочь?)", reply_markup=markup)
    elif(message.text == "Нет"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        button3 = types.KeyboardButton("🆘HELP🆘")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "❓ Задать вопрос"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Как тебя зовут?")
            btn2 = types.KeyboardButton("Что ты можешь?")
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text="Задай мне вопрос ...", reply_markup=markup)

    elif (message.text == "Как тебя зовут?"):
            bot.send_message(message.chat.id, "Меня зовут БДэшечка ")

    elif message.text == "Что ты можешь?":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("🔍 Поиск в Wikipedia")
            button2 = types.KeyboardButton("📚 Документация")
            button3 = types.KeyboardButton("📕 Скачать книгу")
            button4 = types.KeyboardButton("🏃 Квест")
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(button1,button2, button3,button4, back)
            bot.send_message(message.chat.id, text="Поздороваться с читателями\nОтправить учебник \nРассказать многое о БД и СУБД",reply_markup=markup)

    elif message.text == "📕 Скачать книгу":
            bot.send_message(message.from_user.id, "подожди \nЗагружаю книгу...")
            f = open(r'СУБД учебник.pdf', 'rb')
            bot.send_document(message.chat.id, f, timeout=150)

    elif (message.text == "Вернуться в главное меню"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("👋 Поздороваться")
            button2 = types.KeyboardButton("❓ Задать вопрос")
            button3 = types.KeyboardButton("🆘HELP🆘")
            markup.add(button1, button2, button3)
            bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "🆘HELP🆘"):
            bot.send_message(message.chat.id, "Я бот который может \nОтправить учебник \nРассказать многое о БД и СУБД")
    else:
        documents(message)
def documents(message):
    if message.text == "📚 Документация":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1 раздел")
        button2 = types.KeyboardButton("2 раздел")
        button3 = types.KeyboardButton("3 раздел")
        button4 = types.KeyboardButton("4 раздел")
        button5 = types.KeyboardButton("5 раздел")
        button6 = types.KeyboardButton("6 раздел")
        button7 = types.KeyboardButton("7 раздел")
        back = types.KeyboardButton("Вернуться назад")
        markup.add(button1, button2, button3, button4, button5, button6, button7, back)
        bot.send_message(message.chat.id, text="Выбери раздел книги, чтобы узнать больше", reply_markup=markup)
    elif message.text =="Вернуться назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("🔍 Поиск в Wikipedia")
        button2 = types.KeyboardButton("📚 Документация")
        button3 = types.KeyboardButton("📕 Скачать книгу")
        button4 = types.KeyboardButton("🏃 Квест")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id,text="Вы вернулись в меню с функциями",reply_markup=markup)
    elif message.text == "1 раздел":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1.1 История развития представлений о БД")
        button2 = types.KeyboardButton("1.2 Основные функции и типовая организаци современной СУБД")
        button3 = types.KeyboardButton("1.3 Ранние подходы к организации СУБД")
        button4 = types.KeyboardButton("1.4 Общие понятие реляционного подхода к организации БД")
        button5 = types.KeyboardButton("1.5")
        button6 = types.KeyboardButton("1.6")
        back = types.KeyboardButton("Назад в разделы")
        markup.add(button1, button2, button3, button4, button5, button6, back)
        bot.send_message(message.chat.id, text="Выбери раздел книги, чтобы узнать больше", reply_markup=markup)

    elif message.text == "1.1 История развития представлений о БД":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Банк данных")
        button2 = types.KeyboardButton("ИС(Информационная система)")
        button3 = types.KeyboardButton("БД(База данных)")
        button4 = types.KeyboardButton("СУБД")
        button5 = types.KeyboardButton("Словарь данных")
        button6 = types.KeyboardButton("Администратор БД")
        button7 = types.KeyboardButton("Вычислительная сиситема")
        back = types.KeyboardButton("Назад в разделы")
        markup.add(button1, button2, button3, button4, button5, button6, button7, back)
        bot.send_message(message.chat.id, text="Выбери раздел книги, чтобы узнать больше", reply_markup=markup)

    elif message.text == "Банк данных":
        bot.send_message(message.chat.id, text="Банк данных является разновидностью ИС, в которой реализованы функции централизованного хранения и накопления обрабатываемой информации, организованной в одну или несколько БД")
    elif message.text == "ИС(Информационная система)":
        bot.send_message(message.chat.id, "ИС(Информационная система) - это аппаратно-программные средства, задействованные для решения некоторых прикладных")
    elif message.text == "БД(База данных)":
        bot.send_message(message.chat.id, "БД представляет собой совокупность специальным образом организованных данных, хранимых в памяти ВС и отображающих состояние объектов и их взаимосвязи в рассматриваемой предметной области")
    elif message.text == "СУБД":
        bot.send_message(message.chat.id, "СУБД — комплекс языковых и программных средств, предназначенных для создания, ведения и совместного использования БД многими пользователями")
    elif message.text == "Словарь данных":
        bot.send_message(message.chat.id, "Словарь данных представляет собой подсистему банка данных, предназначенную для централизованного хранения информации о структурах данных, взаимосвязях файлов, \nтипах данных,форматах их представления, принадлежности данных пользователя, кодак зашиты и разграничения доступа.")
    elif message.text == "Администратор БД":
        bot.send_message(message.chat.id, "Администратор БД — лицо или группа лиц, отвечающая за выбор требований к БД, ее проектирование. создание, эффективное использование и сопровождение.")
    elif message.text == "Вычислительная система":
        bot.send_message(message.chat.id, "Вычислительная система представляет собой совокупность взаимосвязанных и согласованно действующих ЭВМ, процессора и других устройств, обеспечивающих автоматизацию процессов приема, обработки и выдачи информации потребителю")

    elif message.text == "1.2 Основные функции и типовая организаци современной СУБД":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Основные функции современной СУБД")
        button2 = types.KeyboardButton("1.Непосредственное управление данными во внешней памяти")
        button3 = types.KeyboardButton("2.Управление буферами оперативной памяти")
        button4 = types.KeyboardButton("3.Управление транзакциями")
        button5 = types.KeyboardButton("4.Журнализация")
        button6 = types.KeyboardButton("5.Поддержка языков БД")
        button7 = types.KeyboardButton("Типовая организация современной СУБД")
        back = types.KeyboardButton("Назад в разделы")
        markup.add(button1, button2, button3, button4, button5, button6, button7, back)
        bot.send_message(message.chat.id, text="Выбери раздел книги, чтобы узнать больше", reply_markup=markup)

    elif message.text == "Назад в разделы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1 раздел")
        button2 = types.KeyboardButton("2 раздел")
        button3 = types.KeyboardButton("3 раздел")
        button4 = types.KeyboardButton("4 раздел")
        button5 = types.KeyboardButton("5 раздел")
        button6 = types.KeyboardButton("6 раздел")
        button7 = types.KeyboardButton("7 раздел")
        back = types.KeyboardButton("Вернуться назад")
        markup.add(button1, button2, button3, button4, button5, button6, button7, back)
        bot.send_message(message.chat.id, text="Вы вернулись назад", reply_markup=markup)
    else:
        kvest(message)

def wiki_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("🔍 Поиск в Wikipedia")
    button2 = types.KeyboardButton("📚 Документация")
    button3 = types.KeyboardButton("📕 Скачать книгу")
    button4 = types.KeyboardButton("🏃 Квест")
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(button1, button2, button3, button4, back)
    bot.send_message(message.from_user.id, getwiki(message.text), reply_markup=markup)
    bot.send_message(message.from_user.id, "Вот что нашлось по вашему запросу")
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2 =re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом'

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    btn3 = types.KeyboardButton("🆘HELP🆘")
    markup.add(btn2, btn3)
    bot.send_message(message.from_user.id, 'Привет, {0.first_name}! Меня зовут БДэшечка,я помогу тебе с Базой данных и Системами управления баз данных!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text', 'document', 'audio'])
def text_message(message):
    if message.text == "🔍 Поиск в Wikipedia":
        bot.send_message(message.from_user.id, '{0.first_name}, отправь мне любое слово, и я найду его значение на Wikipedia'.format(message.from_user))
        bot.register_next_step_handler(message, wiki_text)
    else:
        get_text_messages(message)
bot.polling(none_stop=True, interval=0)