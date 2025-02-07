import pymysql

# Подключение к базе данных
connection = pymysql.connect(
    host="mysql-rfam-public.ebi.ac.uk",
    user="rfamro",
    password="",
    database="Rfam",
    port=4497
)

try:
    with connection.cursor() as cursor:
        # Проверка доступных таблиц
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Доступные таблицы:", tables)

        # Пробуем запрос к другой таблице, если fram_acc недоступна
        cursor.execute("SELECT * FROM full_region LIMIT 1;")
        result = cursor.fetchall()
        print("Результат запроса:", result)

finally:
    connection.close()

with open("output.txt", "w") as f:
    for row in result:
        f.write(str(row) + "\n")

print("Результат сохранён в файл: output.txt")
