import json
from datetime import datetime, timedelta
import random

# Параметры генерации
words = ['dog', 'cat', 'mouse', 'bird', 'elephant', 'tiger', 'lion', 'horse', 'wolf', 'bear']
translations = {
    'dog': 'собака,пес',
    'cat': 'кот,кошка,кошак',
    'mouse': 'мышь',
    'bird': 'птица',
    'elephant': 'слон',
    'tiger': 'тигр',
    'lion': 'лев',
    'horse': 'лошадь',
    'wolf': 'волк',
    'bear': 'медведь'
}
examples = {
    'dog': 'I like dogs',
    'cat': 'Cats are strange',
    'mouse': 'The mouse ran away',
    'bird': 'Birds are singing',
    'elephant': 'Elephants are huge',
    'tiger': 'Tigers are dangerous',
    'lion': 'Lions are the kings of the jungle',
    'horse': 'Horses are fast runners',
    'wolf': 'Wolves are pack animals',
    'bear': 'Bears are strong'
}

num_records = 10000  # Количество записей
start_date = datetime.today()  # Начальная дата (сегодня)
date_range = 365  # Диапазон дат (+/- 1 год)

data = []

for _ in range(num_records):
    word = random.choice(words)
    repeat_after = random.randint(0, 30)
    repeat_date = start_date + timedelta(days=random.randint(-date_range, date_range))

    entry = {
        'word': word,
        'translations': translations[word],
        'example': examples[word],
        'repeat_count': 0,
        'repeat_after': repeat_after,
        'repeat_date': repeat_date.strftime('%Y-%m-%d')
    }

    data.append(entry)

# Сохраняем данные в JSON файл
with open('words_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

'Файл сгенерирован успешно.'
