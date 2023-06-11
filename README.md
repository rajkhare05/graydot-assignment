# Graydot Assignment

All the requests are sent to the `/api/tasks` endpoint and its child routes.\
Pagination is also supported.

### Project setup

1. Clone this repository. \
`git clone https://github.com/rajkhare05/graydot-assignment.git`

2. Create an virtual environment. \
`python -m venv env`

3. Activate the virtual environment. \
Linux: `source env/bin/activate`

4. Install the dependencies. \
`pip install -r requirements.txt`

5. Run `python run.py` to start.

### Docs

- Get all tasks.

  **GET** `/api/tasks`
  ```sh
  curl "http://127.0.0.1:5000/api/tasks"
  ```
  By default all tasks are returned (as `page=1&limit={total_tasks}` is set). \
  **To use pagination: use `page` and `limit` query parameters.**
  
- Get a task by id.

  **GET** `/api/tasks/{id}`
  ```sh
  curl "http://127.0.0.1:5000/api/tasks/1"
  ```
  Response:
  ```js
  {
    "description": "Make your mindset to learn java",
    "due_date": "01-06-2023",
    "id": 1,
    "status": "Completed",
    "title": "Nightmare just became true"
  }
  ```
  
- Create a new task.

  **POST** `/api/tasks/new`
  ```sh
  curl -X POST http://127.0.0.1:5000/api/tasks/new -H "Content-Type: application/json" -d '{ 
      "title": "Complete Project Proposal",
      "description": "Write a detailed project proposal outlining the goals and objectives.",
      "due_date": "18-06-2023",
      "status": "Incomplete"
  }'
  ```
  Response:
  ```js
  {
     "id": 1,
     "message": "Task created"
  }
  ```

- Update the task with task id in the path.

  **PATCH** `/api/tasks/{id}`
  ```sh
  curl -X PATCH "http://127.0.0.1:5000/api/tasks/1" -H "Content-Type: application/json" -d '{
     "status": "Completed"
  }'
  ```
  Response:
  ```js
  {
    "message":"Task updated"
  }
  ```

- Delete a task by id.

  **DELETE** `/api/tasks/{id}`
  ```sh
  curl -X DELETE "http://localhost:5000/api/tasks/1"
  ```
  Response:
  ```js
  {
     "message": "Task deleted"
  }
  ```

