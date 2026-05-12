from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {'id': 1, 'name': 'Hamza', 'grade': 'A'},
    {'id': 2, 'name': 'Ahmed', 'grade': 'B'},
]
next_id = 3

@app.route('/api/students', methods=['GET'])
def get_student():
    return jsonify(students), 200

@app.route('/api/students/<int:sid>', methods=['GET'])
def get_one(sid):
    # Use 'None' with a capital N
    s = next((s for s in students if s['id'] == sid), None)
    if s:
        return jsonify(s), 200
    else:
        return jsonify({'error': 'Not found'}), 404
        
@app.route('/api/student/', methods=['POST'])
def add_student():
    global next_id
    # Changed jsonify.get_requet() to request.get_json()
    data = request.get_json()

    if not data or 'name' not in data or 'grade' not in data:
        return jsonify({'error': 'name and grade required'}), 400
                
    new_student = {
        'id': next_id, 
        'name': data['name'], 
        'grade': data['grade']
    }
        
    students.append(new_student)
    next_id += 1
    return jsonify(new_student), 201

#
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)