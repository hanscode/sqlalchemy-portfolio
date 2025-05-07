from flask import render_template, url_for, request, redirect

from models import db, Project, app
import datetime


def clean_completion_date(date_str):
    """
    Turn a 'YYYY-MM' string into a datetime.date object (using day=1).
    """
    year, month = date_str.split('-')
    return datetime.date(int(year), int(month), 1)

   

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/new', methods=['GET', 'POST'])
def add_project():
    
    if request.form:
        print(request.form)
        print(request.form['title'])
        raw_date = request.form['date']
        new_project = Project(
            title=request.form['title'],
            completion_date=clean_completion_date(raw_date),
            description=request.form['desc'],
            skills=request.form['skills'],
            github=request.form['github']
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new.html')


@app.route('/project/<id>')
def project_detail(id):
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project)


@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get_or_404(id)
    if request.form:
        raw_date = request.form['date']
        project.title = request.form['title']
        project.completion_date = clean_completion_date(raw_date)
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.github = request.form['github']
        db.session.commit()
        return redirect(url_for('project_detail', id=id))
    return render_template('edit.html', project=project)

@app.route('/project/<id>/delete', methods=['GET'])
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.1')