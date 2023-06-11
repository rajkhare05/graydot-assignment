from flask_sqlalchemy import SQLAlchemy
import enum
from marshmallow import Schema, fields, validate

db = SQLAlchemy()


class StatusType(enum.Enum):
    INCOMPLETE = "Incomplete"
    COMPLETED = "Completed"
    IN_PROGRESS = "In Progress"


class TaskSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=5, max=100))
    description = fields.String(required=True, validate=validate.Length(min=5))
    due_date = fields.Date(format="%d-%m-%Y", required=True)
    status = fields.String(required=True, validate=validate.OneOf([status.value for status in StatusType]))


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.Date(), nullable=False)
    status = db.Column(db.String(11), nullable=False)

    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
