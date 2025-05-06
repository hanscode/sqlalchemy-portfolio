# Python Web Development Techdegree  
### Project 5 - Portfolio with SQLAlchemy  
**Author** - Hans Steffens  

## Project Overview

This is a Python portfolio web application. The main (index) page lists your projects including the project title and short description. Each project links to a detail page that displays the title, date, and description. 

The application lets the user add or edit project information. When adding or editing a project, the application prompts the user for title, date, skills, description, and a link to a repo. The results for these entries are stored in a database and displayed on the homepage

## Tools and Technologies Used

- Python 3.12
- Flask 3.1.0
- SQLAlchemy 2.0 (ORM for database interaction)
- SQLite (local database)
- Datetime module (for handling dates and timestamps)

## Getting Started
Follow these steps to set up and run the application locally.

### 1. Clone the Repository
```bash
git clone https://github.com/hanscode/sqlalchemy-portfolio.git
cd sqlalchemy-portfolio
```

### 2. Set Up a Virtual Environment
Create a virtual environment to isolate project dependencies:

```bash
python -m venv env
```

### 3. Activate the Virtual Environment
Create a virtual environment to isolate project dependencies:

- On Mac/Linux:
```bash
source ./env/bin/activate
```
- On Windows:
```bash
.\env\Scripts\activate
```
You should now see the environment activated, e.g., `(env)` in your terminal prompt.

### 4. Install Project Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```
### 5. Run the Application
Once inside the project folder and with your virtual environment active:

```sh
python app.py
```
You will see the application menu and can start interacting with the inventory!


## License
This project is licensed under the [MIT LICENSE](LICENSE).