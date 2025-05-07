from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Date
import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db"
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    title = db.Column('Project Title', db.String())
    completion_date = db.Column('Completion Date', Date)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.String())
    github = db.Column('GitHub URL', db.String())

    def __repr__(self):
        return f'''
        <Project {self.id}>
        <Project Title: {self.title}>
        <Completion Date: {self.completion_date}>
        <Description: {self.description}>
        <Skills: {self.skills}>
        <GitHub URL: {self.github}>
        '''
