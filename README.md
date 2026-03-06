# Vulnerable Web Lab

## 🔹 Objetivo

Este laboratorio web está diseñado para practicar **pentesting y seguridad ofensiva**. Incluye vulnerabilidades reales que se pueden explotar para aprender cómo funcionan y cómo mitigarlas.  

Ideal para **portfolios de ciberseguridad** y para practicar habilidades de **red team**.

---

## 🔹 Arquitectura

- **Reverse Proxy:** Nginx
- **Web App:** Python + Flask
- **Base de datos:** MySQL
- **Contenedores:** Docker + Docker Compose


---

## 🔹 Endpoints y vulnerabilidades

| Endpoint | Vulnerabilidad | Descripción |
|----------|----------------|-------------|
| `/login` | Broken Authentication | Login inseguro, contraseñas en claro, bypass posible |
| `/search` | SQL Injection | Inyección en parámetros GET/POST |
| `/profile/<id>` | IDOR | Acceso a perfiles de otros usuarios |
| `/comment` | XSS | Reflejado o persistente, permite inyección de scripts |
| `/ping` | Command Injection | Inyección de comandos en el servidor |
| `/download/<file>` | Path Traversal | Acceso a archivos fuera del directorio seguro |
| `/admin` | Broken Auth / Misconfiguration | Endpoint con privilegios elevados |

---

## 🔹 Base de datos inicial (MySQL)

### Tabla `users`

| id | username | password | role  |
|----|---------|----------|-------|
| 1  | admin   | admin123 | admin |
| 2  | alice   | pass123  | user  |
| 3  | bob     | bobpass  | user  |

### Tabla `comments`

| id | user_id | comment |
|----|--------|---------|
| 1  | 2      | Hello!  |
| 2  | 3      | Test    |

---

## 🔹 Cómo se explotaría

- **SQL Injection:** `/login` o `/search` con payloads `' OR '1'='1`  
- **XSS:** `/comment` enviando `<script>alert(1)</script>`  
- **IDOR:** `/profile/2` desde otro usuario  
- **Command Injection:** `/ping?host=;ls`  
- **Path Traversal:** `/download/../../etc/passwd`  
- **Broken Auth:** login con contraseñas por defecto o bypass de session  

> ⚠️ Este laboratorio es solo para **práctica en entornos controlados**. Nunca usarlo en producción.

---

## 🔹 Estructura del proyecto

vulnerable-web-lab/
│
├── docker/
│   ├── nginx/          # Configuración reverse proxy
│   └── mysql/          # Configuración MySQL + datos iniciales
│
├── app/
│   ├── routes/         # Cada endpoint vulnerable como archivo separado
│   ├── templates/      # HTML + Bootstrap
│   ├── static/         # JS, CSS
│   └── app.py          # Flask main
│
├── exploits/           # Scripts de explotación
│   ├── sql_injection/
│   ├── xss/
│   └── idor/
│
├── docs/               # Guías y writeups
│   ├── sql_injection.md
│   ├── xss.md
│   └── idor.md
│
├── docker-compose.yml
├── setup.sh            # Inicialización de DB, creación de usuarios
└── README.md

