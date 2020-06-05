# Python Flask REST API for Tasks

## Software Configuration Management (SCM)
This repo can be cloned as follows:
```
   $ git clone https://github.com/dlwhitehurst/tasks.git
```

## Configure and Run
First obtain the required Python modules using pip to install:
``` 
   $ pip install -r requirements.txt`
```
Next, run the application with:
```
   $ python app.py
``` 
## Endpoints

- POST   /api/vi/tasks
- GET    /api/v1/tasks
- GET    /api/v1/tasks/{taskId}
- PUT    /api/v1/tasks/{taskId}
- DELETE /api/v1/tasks/{taskId}

## Command-line testing
To obtain a listing of all Tasks, call GET /api/v1/tasks:

    curl -i -X GET "http://localhost:5000/api/v1/tasks"
    ---
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 350
    Server: Werkzeug/1.0.1 Python/3.7.7
    Date: Fri, 05 Jun 2020 02:37:05 GMT
    
    {
      "tasks": [
        {
          "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
          "done": false,
          "id": 1,
          "title": "Buy groceries"
        },
        {
          "description": "Need to create a Python Flask Dockerized Container (REST API)",
          "done": false,
          "id": 2,
          "title": "Learn Python Flask Development"
        }
      ]
    }
