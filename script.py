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
        # Выполнение простого запроса
        cursor.execute("SELECT * FROM fr.fram_acc LIMIT 1;")
        result = cursor.fetchall()
        print("Результат запроса:", result)

        # Выполнение сложного запроса
        query = """
        SELECT fr.rfam_acc, fr.rfamseq_acc, fr.seq_start, fr.seq_end
        FROM full_region fr, rfamseq rf, taxonomy tx
        WHERE rf.ncbi_id = tx.ncbi_id
          AND fr.rfamseq_acc = rf.rfamseq_acc
          AND tx.ncbi_id = 10116
          AND is_significant = 1
        """
        cursor.execute(query)
        result = cursor.fetchall()
        print("Результат сложного запроса:", result)
finally:
    connection.close()
