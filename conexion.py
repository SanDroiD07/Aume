from mysql.connector import connect, Error
import os

def create_connection():
    try:
        connection = connect(
            host=os.getenv("DB_SERVERNAME"),
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except Error as e:
        print(f"Error: '{e}'")

# Ejemplo de uso
if __name__ == "__main__":
    connection = create_connection()
    # Aquí puedes continuar con tu código para interactuar con la base de datos