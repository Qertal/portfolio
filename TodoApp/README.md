# TodoApp

TodoApp is an application designed for task management. It allows users to create, edit, delete, and mark tasks as completed. It supports user registration and login, as well as task management through an intuitive interface based on HTML and Bootstrap.

## Features

- User registration and login
- Creating new tasks
- Editing existing tasks
- Deleting tasks
- Marking tasks as completed

## Technologies Used

- **FastAPI** – framework for building APIs
- **Uvicorn** – ASGI server
- **MySQL** – database (easily replaceable with SQLite)
- **Bootstrap** – for styling the user interface
- **HTML** – frontend templates
- **Pytest** – testing framework

## Installation and Running

1. Clone the repository:
   ```bash
   git clone https://github.com/qertal/TodoApp.git
   cd TodoApp
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the database (default is MySQL):
   - In tables.sql file you have queries to generate tables.
   OR
   - Modify the `database.py` file if you wish to use a different database (e.g., SQLite).

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Open the application in your browser at:
   ```
   http://127.0.0.1:8000
   ```

## Testing

To run tests:

```bash
pytest
```

Tests cover basic functionalities such as:
- Adding users
- Deleting users
- Managing tasks

