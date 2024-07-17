import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="perpustakaan"
    )
    try:
        yield conn
    finally:
        conn.close()

def create_table():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS buku (
                id INT AUTO_INCREMENT PRIMARY KEY,
                judul VARCHAR(255),
                penulis VARCHAR(255),
                penerbit VARCHAR(255),
                tahun_terbit INT,
                konten TEXT,
                iktisar TEXT
            )
        """)
        conn.commit()
        cursor.close()

create_table()

def get_buku(judul):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM buku WHERE judul = %s"
        cursor.execute(query, (judul,))
        result = cursor.fetchone()
        cursor.close()
    if result:
        return Buku(result[1], result[2], result[3], result[4], result[5].split(","), result[6])
    return None

def post_buku(buku):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = """
            INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, konten, iktisar)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, ",".join(buku.konten), buku.iktisar))
        conn.commit()
        cursor.close()
