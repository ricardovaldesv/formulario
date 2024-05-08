# Application Setup

![](/frontend/public/photoApp.png)

This guide outlines the steps to set up the fomr application, along with configuring a PostgreSQL database.

## Frontend Setup

### Prerequisites
-  Make sure you have Node.js version 14.21.3 or later, npm version 6.14.18 or later installed on your machine, boostrap and Material-UI.

### Installation
1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Instal boostrap: `npm install bootstrap`
4. Instal Material-UI: `npm install @mui/material @emotion/react @emotion/styled`


## Backend Setup

### Prerequisites
- Python 3.10 or later installed on your machine
- PostgreSQL 14.11 or later installed and running

### Database Setup
1. Install PostgreSQL: Follow the official documentation or use your package manager.
2. Once PostgreSQL is installed, access the psql command line interface executing the following command on your terminal:
  ```bash
   sudo -u postgres psql
  ```
3. Execute the script provided **database_setup.sql**

### Virtual Environment
1. Navigate to the backend directory: `cd backend`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

### Install Dependencies
1. Ensure the virtual environment is activated.
2. Install dependencies from requirements.txt: `pip install -r requirements.txt`

### Django Migration
1. Create Initial Migrations: `python manage.py makemigrations`
2. Apply migrations to the database: `python manage.py migrate`

### Finally
1. Start the Django development server: `python manage.py runserver`
2. Start the React development server: `npm start`
3. Access the frontend at `http://localhost:3000` and the backend at `http://localhost:8000/admin`.
