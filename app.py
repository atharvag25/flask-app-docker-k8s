
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    roll_no = request.form['roll_no']
    course = request.form['course']

    students.append({
        'name': name,
        'roll_no': roll_no,
        'course': course
    })

    return redirect('/')

@app.route('/delete/<int:index>')
def delete_student(index):
    if 0 <= index < len(students):
        students.pop(index)

    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
