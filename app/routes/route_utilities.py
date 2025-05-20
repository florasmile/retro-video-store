from flask import abort, make_response, Response
from ..db import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        invalid = {"message": f"{cls.__name__} id {model_id} is invalid."}
        abort(make_response(invalid, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        not_found = {"message": f"{cls.__name__} {model_id} was not found"}
        abort(make_response(not_found, 404))
    return model


def create_response_for_model(cls, model_data):
    try:
        new_model = cls.from_dict(model_data)
    except KeyError as err:
        response = {"details": f"Request body must include {err.args[0]}."}
        abort(make_response(response, 400))
    db.session.add(new_model)
    db.session.commit()

    return new_model.to_dict(), 201

def update_model(model, model_data):
    try:
        model.update(model_data)
    except KeyError as err:
        response = {"details": f"Invalid data"}
        abort(make_response(response, 400))

    db.session.commit()

    return Response(status=204, mimetype="application/json")
