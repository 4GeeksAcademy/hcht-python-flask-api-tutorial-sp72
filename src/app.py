from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    # json_text = jsonify(todos)
    return todos, 200


@app.route('/todos', methods=['POST'])
def add_new_todo():
    data = request.json
    todos.append(data)
    print('Incoming request with the followint body', data)
    print('todos', todos)
    return todos


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    print('This is the positon to delete:', position)
    return todos


some_data = {"name": "Bobby", "lastname": "Rixer"}
todos = [{"label": "My first task", "done": False}]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
