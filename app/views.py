from flask import Blueprint, jsonify, request
from .models import Task, db
from .models import TaskSchema
from marshmallow import ValidationError


api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/tasks", methods=["GET"])
def get_tasks():
    try:
        total_tasks = Task.query.count()
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", total_tasks))
        offset = (page - 1) * limit
        tasks = Task.query.offset(offset).limit(limit).all()
        task_list = []

        for task in tasks:
            new_task = {"id": task.id, "title": task.title, "description": task.description, "due_date": task.due_date.strftime("%d-%m-%Y"), "status": task.status}
            task_list.append(new_task)

        return jsonify({"tasks": task_list})

    except ValueError:
        return jsonify({"message": "Invalid page or limit"}), 400


@api_blueprint.route("/tasks/new", methods=["POST"])
def create_new_task():
    data = request.json
    task_schema = TaskSchema()
    try:
        task_data = task_schema.load(data)
        task = Task(**task_data)
        db.session.add(task)
        db.session.commit()
        return jsonify({"id": task.id, "message": "Task created"})

    except ValidationError as err:
        return jsonify({"message": err.messages}), 400


@api_blueprint.route("/tasks/<int:id>", methods=["GET"])
def get_task_by_id(id):
    task = Task.query.get(id)

    if task:
        return jsonify({"id": task.id, "title": task.title, "description": task.description, "due_date": task.due_date.strftime("%d-%m-%Y"), "status": task.status})

    return jsonify({"message": "Task not found"}), 404


@api_blueprint.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task_by_id(id):
    task = Task.query.get(id)

    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted"})

    return jsonify({"message": "Task not found"}), 404


@api_blueprint.route("/tasks/<int:id>", methods=["PATCH"])
def update_task_by_id(id):
    task = Task.query.get(id)
    if task:
        data = request.json
        try:
            task_schema = TaskSchema(partial=True)
            task_data = task_schema.load(data)
        except ValidationError as err:
            return jsonify({"message": err.messages}), 400

        task.title = task_data.get("title", task.title)
        task.description = task_data.get("description", task.description)
        task.due_date = task_data.get("due_date", task.due_date)
        task.status = task_data.get("status", task.status)

        db.session.commit()
        return jsonify({"message": "Task updated"})

    return jsonify({"message": "Task not found"}), 404
