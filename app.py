#!flask/bin/python

# Flask
from flask import Flask, jsonify, abort, make_response, request

# Swagger ( https://editor.swagger.io/ )
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python Flask Development',
        'description': u'Need to create a Python Flask Dockerized Container (REST API)',
        'done': False
    }
]

#----------------------------------------------------------------------------#
# Static Swagger Rendering.
#----------------------------------------------------------------------------#
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Python Flask Tasks API"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

#----------------------------------------------------------------------------#
# API Method Implementations.
#----------------------------------------------------------------------------#
@app.route('/api/v1/tasks', methods=['GET'])
def get_tasks():
    return {'tasks': tasks} # no need to use jsonify (less code) return dict
#    return jsonify({'tasks': tasks})

@app.route('/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return {'task': task[0]}

@app.route('/api/v1/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return {'task': task}, 201

@app.route('/api/v1/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return {'task': task[0]}

@app.route('/api/v1/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return {'result': True}

#----------------------------------------------------------------------------#
# Error Handling.
#----------------------------------------------------------------------------#
@app.errorhandler(400)
def bad_request(error):
     return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
     return make_response(jsonify({'error': 'Not Found'}), 404)

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug=True)
