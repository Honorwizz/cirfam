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

        # Выполнение простого запроса
        try:
            cursor.execute("SELECT * FROM fr.fram_acc LIMIT 1;")
            result = cursor.fetchall()
            print("Результат простого запроса:", result)
        except pymysql.err.OperationalError as e:
            print("Ошибка выполнения простого запроса:", e)

        # Выполнение сложного запроса
        try:
            query = """
            SELECT fr.rfam_acc, fr.rfamseq_acc, fr.seq_start, fr.seq_end
            FROM full_region fr, rfamseq rf, taxonomy tx
            WHERE rf.ncbi_id = tx.ncbi_id
              AND fr.rfamseq_acc = rf.rfamseq_acc
              AND tx.ncbi_id = 10116 -- NCBI taxonomy id of Rattus norvegicus
              AND is_significant = 1 -- exclude low-scoring matches from the same clan
            """
            cursor.execute(query)
            result = cursor.fetchall()
            print("Результат сложного запроса:", result)
        except pymysql.err.OperationalError as e:
            print("Ошибка выполнения сложного запроса:", e)

finally:
    connection.close()
    print("Соединение с базой данных закрыто.")
