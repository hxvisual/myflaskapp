from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)

# Конфигурация
app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница проектов
@app.route('/projects')
def projects():
    projects = [
        {
            'title': 'Проект 1',
            'description': 'Описание первого проекта',
            'image': 'project1.jpg',
            'link': '#'
        },
        {
            'title': 'Проект 2',
            'description': 'Описание второго проекта',
            'image': 'project2.jpg',
            'link': '#'
        }
    ]
    return render_template('projects.html', projects=projects)

# Страница контактов
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Здесь можно добавить логику отправки письма
        print(f"Получено сообщение от {name} ({email}): {message}")
        return redirect(url_for('contact_success'))
    return render_template('contact.html')

@app.route('/contact/success')
def contact_success():
    return render_template('contact.html', success=True)

if __name__ == '__main__':
    app.run(debug=True)