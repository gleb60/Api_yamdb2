import csv
import sqlite3
 
# Подключение к базе данных
conn = sqlite3.connect('api_yamdb\db.sqlite3')
cursor = conn.cursor()
 
# Список файлов CSV для загрузки
static_data = ['api_yamdb\static\data\category.csv',
             'api_yamdb\static\data\comments.csv',
             'api_yamdb\static\data\genre_title.csv',
             'api_yamdb\static\data\genre.csv',
             'api_yamdb\static\data\review.csv',
             'api_yamdb\static\data\titles.csv',
             'api_yamdb\static\data\users.csv',]
 
# Цикл по файлам CSV
for csv_data in static_data:
    # Чтение данных из CSV файла
    with open(csv_data, 'r') as data:
        csv_reader = csv.reader(data)
        next(csv_reader)  # Пропуск заголовка, если он есть
 
        # Цикл по строкам CSV файла
        for row in csv_reader:
            cursor.execute('INSERT INTO table_name (column1, column2, column3) VALUES (?, ?, ?)', (row[0], row[1], row[2]))
 
# Сохранение изменений и закрытие соединения с базой данных
conn.commit()
conn.close()