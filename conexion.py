from flask import Flask, jsonify
from mysql.connector import connect, Error
import os

app = Flask(__name__)

def create_connection():
    try:
        connection = connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME"),
        )
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