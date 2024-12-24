# Finance Web App

This is a Django-based finance web application that utilizes MySQL as its database. The application is designed to manage financial data and provide various functionalities related to finance management.

## Project Structure

```
finance-web-app
├── finance_app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── finance_web_app
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── db.sqlite3
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd finance-web-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   Update the `DATABASES` setting in `finance_web_app/settings.py` to connect to your MySQL database.

5. **Run migrations:**
   ```
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```
   python manage.py runserver
   ```

## Usage

Access the application by navigating to `http://127.0.0.1:8000/` in your web browser. You can log in to the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials you created.

## Contributing

Feel free to submit issues or pull requests for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.