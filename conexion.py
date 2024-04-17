from flask import Flask, jsonify
from mysql.connector import connect, Error
import os

app = Flask(__name__)

def create_connection():
    try:
        connection = connect(
            user="Sandro",
            password=os.getenv("DB_PASS"),
            host="college.mysql.database.azure.com",
            port=3306,
            database=os.getenv("DB_NAME"),
            ssl_ca="{ca-cert filename}",
            ssl_disabled=False
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except Error as e:
        print(f"Error: '{e}'")

@app.route('/padres', methods=['GET'])
def get_padres():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM padres")
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == "__main__":
    app.run()