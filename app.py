from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask API!"

@app.route('/student')
def get_student():
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Sai Zen Soti-ar"
    })

# ✅ Dynamic route for student info
@app.route('/student_info')
def get_student_info():
    # Get query parameters (with defaults)
    name = request.args.get('name', 'Unknown')
    grade = request.args.get('grade', 'N/A')
    bmi = request.args.get('bmi', 'N/A')
    address = request.args.get('address', 'Not Provided')
    gender = request.args.get('gender', 'Not Specified')
    age = request.args.get('age', 'N/A')

    return jsonify({
        "name": "Sai Zen",
        "grade": 15,
        "bmi": bmi,
        "address": "Salngan Passi City",
        "gender": "Male",
        "age": 21
    })

if __name__ == '__main__':
    app.run(debug=True)
