from flask import Flask, request, render_template
import mysql.connector
import os
from db import get_db_connection

app = Flask(__name__)

# Configuración DB desde variables de entorno
DB_HOST = os.environ.get("DB_HOST", "db")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASS = os.environ.get("DB_PASS", "rootpass")
DB_NAME = os.environ.get("DB_NAME", "vulnerable_lab")

@app.route("/") # para probar que la conexión funciona
def index():
    return "App is running"
    
@app.route("/users")
def list_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM users")
        users = cursor.fetchall()
        return "<br>".join([f"{user[0]}: {user[1]}" for user in users])
    except Exception as e:
        return f"Error fetching users: {e}"
    
@app.route("/login", methods=["POST", "GET"])       # Login Bypass Vulnerable a SQL Injection
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            # Vulnerable a SQL Injection
            query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
            cursor.execute(query)
            user = cursor.fetchone()
            if user:
                return "Login successful!"
            else:
                return "Invalid credentials."
        except Exception as e:
            return f"Error during login: {e}"
    return render_template("login.html") # Página de login simple con un formulario

@app.route("/search")       # Search Vulnerable a SQL Injection, permite buscar usuarios por nombre
def search_user():
    username = request.args.get("username")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Vulnerable a SQL Injection
        query = f"SELECT username, role FROM users WHERE username = '{username}'"

        cursor.execute(query)
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        # output = "<h2>Search Results:</h2><ul>"
        # for row in users:
        #     output += f"<li>Username: {row[0]}, Role: {row[1]}</li>"
        # output += "</ul>"
        return render_template("search.html", user=users) # Página de resultados de búsqueda simple
    except Exception as e:
        return f"Error during search: {e}"
    
@app.route("/profile/<int:user_id>")    # IDOR Vulnerable, permite acceder al perfil de cualquier usuario cambiando el ID en la URL
def profile(user_id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, username, role FROM users WHERE id=%s", # No es vulnerable a SQL Injection porque se usan parámetros, pero es vulnerable a IDOR porque no hay control de acceso
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("profile.html", user=user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)