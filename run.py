from app import Flask_App, db
from enum import Enum
import json


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value
        return super().default(obj)


app = Flask_App()
app.json_encoder = CustomJSONEncoder

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run()
