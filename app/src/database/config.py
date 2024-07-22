import sys

sys.path.append("..")

TORTOISE_ORM = {
    "connections" : {"default": "postgres://andrew:123@0.0.0.0:5432/postgres"},
    "apps": {
        "models":{
            "models":[
                "app.src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}