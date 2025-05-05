
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

member_list = []
task_list = []


@app.route('/')
def home():
    return "Welcome to the Cleaning Team App!"

@app.route('/api/members', methods=['GET', 'POST', 'DELETE'])
def manage_members():
    global member_list
    if request.method == 'GET':
        return jsonify(member_list)
    elif request.method == 'POST':
        new_member = request.json
        member_list.append(new_member)
        return jsonify(new_member)
    elif request.method == 'DELETE':
        member_id = request.json.get('id')
        if not member_id:
            return jsonify({"error": "ID is required"}), 400
        member_list = [member for member in member_list if member['id'] != member_id]
        return jsonify({'message': 'Member deleted'})
    return jsonify({'message': 'Method not allowed'}), 405

@app.route('/api/tasks', methods=['GET', 'POST'])
def manage_tasks():
    global task_list
    if request.method == 'GET':
        return jsonify(task_list)
    elif request.method == 'POST':
        new_task = request.json
        task_list.append(new_task)
        return jsonify(new_task)
    return jsonify({'message': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
