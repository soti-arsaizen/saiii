from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# In-memory student data
students = [
    {"name": "Sai Zen", "grade": 15, "bmi": 21.5, "address": "Salngan Passi City", "gender": "Male", "age": 21}
]

# 🏠 Home page (UI)
@app.route('/')
def home():
    html = """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Student Management</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f7fafc; color: #333; }
            h1 { text-align: center; color: #222; }
            form { background: #fff; padding: 20px; border-radius: 10px; width: 300px; margin: 20px auto; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            input, select, button { width: 100%; padding: 10px; margin: 8px 0; border-radius: 6px; border: 1px solid #ccc; }
            button { background: #007bff; color: white; border: none; cursor: pointer; }
            button:hover { background: #0056b3; }
            .student-list { max-width: 600px; margin: 30px auto; }
            .student-card { background: white; padding: 15px; margin-bottom: 10px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
            .delete-btn { background: #dc3545; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer; float: right; }
            .delete-btn:hover { background: #a71d2a; }
        </style>
    </head>
    <body>
        <h1>📚 Student Management</h1>
        
        <form method="POST" action="/add_student">
            <h3>Add Student</h3>
            <input type="text" name="name" placeholder="Name" required>
            <input type="number" name="grade" placeholder="Grade" required>
            <input type="number" step="0.1" name="bmi" placeholder="BMI" required>
            <input type="text" name="address" placeholder="Address" required>
            <select name="gender" required>
                <option value="">Select Gender</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
            </select>
            <input type="number" name="age" placeholder="Age" required>
            <button type="submit">Add Student</button>
        </form>

        <div class="student-list">
            <h3>Student List</h3>
            {% for s in students %}
                <div class="student-card">
                    <strong>{{ s.name }}</strong> (Grade {{ s.grade }})<br>
                    BMI: {{ s.bmi }} | Age: {{ s.age }} | Gender: {{ s.gender }}<br>
                    Address: {{ s.address }}
                    <form method="POST" action="/delete_student" style="display:inline;">
                        <input type="hidden" name="name" value="{{ s.name }}">
                        <button class="delete-btn" type="submit">Delete</button>
                    </form>
                </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """
    return render_template_string(html, students=students)

# ➕ Add a student
@app.route('/add_student', methods=['POST'])
def add_student():
    new_student = {
        "name": request.form['name'],
        "grade": int(request.form['grade']),
        "bmi": float(request.form['bmi']),
        "address": request.form['address'],
        "gender": request.form['gender'],
        "age": int(request.form['age'])
    }
    students.append(new_student)
    return home()

# ❌ Delete a student by name
@app.route('/delete_student', methods=['POST'])
def delete_student():
    name = request.form['name']
    global students
    students = [s for s in students if s['name'] != name]
    return home()

# 🧩 Optional: JSON API for all students
@app.route('/api/students')
def get_all_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
