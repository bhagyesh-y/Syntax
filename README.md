# Syntax - Django Web Application

A full-stack bloging web application built with Django, featuring a clean UI designed with Bootstrap and custom CSS. This project is currently live and deployed on PythonAnywhere.

**Live Demo:** [https://bhagyeshy.pythonanywhere.com](https://bhagyeshy.pythonanywhere.com)

---

## 🚀 Tech Stack

- **Backend:** Python 3.x, Django Framework
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite3 (Development/Production)
- **Deployment:** PythonAnywhere

---

## 📂 Project Structure

Based on the project's architecture:

- `Syntax/`: The core Django project configuration folder.
- `testapp/`: The primary Django application containing logic, views, and models.
- `templates/`: Global directory for HTML files.
- `dashboards/`: Specific templates or logic for user dashboards.
- `blogs/`: Modules related to blog management/functionality.
- `uploads/`: Directory for media files and user-uploaded content.
- `env/`: Virtual environment settings.
- `db.sqlite3`: The local database file.
- `requirements.txt`: List of Python dependencies.

---

## 🛠️ Installation & Local Setup

To run this project locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-url>
    cd Syntax
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    # On Windows:
    .\env\Scripts\activate
    # On macOS/Linux:
    source env/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
    Access the site at `http://127.0.0.1:8000/`

---

## ☁️ Deployment on PythonAnywhere

This project is configured for PythonAnywhere. Key steps taken for deployment:

1.  Uploaded files via Git/Dashboard.
2.  Configured a VirtualEnv on the PythonAnywhere "Web" tab.
3.  Updated `wsgi.py` to point to the project directory.
4.  Set `DEBUG = False` and added the domain to `ALLOWED_HOSTS` in `settings.py`.
5.  Collected static files using `python manage.py collectstatic`.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Developed by [Bhagyesh]**
