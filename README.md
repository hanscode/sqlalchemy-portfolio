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

## Features

- **Home/List View**  
  Displays all projects with title and short description.  
- **Detail View**  
  Click on a project to see full details: title, completion date, description, skills and GitHub link.  
- **Add Project**  
  Fill out a form to create a new project (title, date, skills, description, repo URL).  
- **Edit Project**  
  Update any existing project via an edit form pre-populated with its current data.  
- **Delete Project**  
  Remove a project from the portfolio.
- **Persistent Storage**  
  SQLite database managed through SQLAlchemy ORM.

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

## Project File Structure
```sh
sqlalchemy-portfolio/
├── LICENSE             # MIT License file
├── README.md           # Project documentation
├── app.py              # Main Flask application with routes
├── instance            # Instance folder (config & DB)
│   └── projects.db     # SQLite database file
├── models.py           # SQLAlchemy models and DB setup
├── requirements.txt    # Python dependencies
├── static              # Static assets folder
│   ├── css             # Stylesheet directory
│   │   └── styles.css  # Custom CSS styles
│   └── images          # Images directory
│       └── headshot.png # Headshot image for About page
└── templates           # Jinja2 templates folder
    ├── 404.html        # Custom 404 error page
    ├── about.html      # About page template
    ├── detail.html     # Project detail page template
    ├── edit.html       # Edit project form template
    ├── index.html      # Home page listing all projects
    ├── layout.html     # Base layout template
    └── new.html        # New project form template
```

## What I Learned

- **Flask Routing & Views**  
  Handling `GET` vs. `POST` requests, dynamic URL parameters, redirects.  
- **Jinja2 Templating**  
  Template inheritance, context processors, looping and string filters in templates.  
- **SQLAlchemy ORM**  
  Defining models, creating sessions, querying, inserting, updating and deleting records.  
- **Form Handling & Validation**  
  Using HTML5 `required` attributes, parsing `input type="month"` into `datetime.date`.  
- **Application Structure**  
  Organizing Flask apps with separate modules for routes, models, static assets, and templates.  
- **User Experience Enhancements**  
  Pre-populating form fields, cancel/reset UX patterns.


## License
This project is licensed under the [MIT LICENSE](LICENSE).