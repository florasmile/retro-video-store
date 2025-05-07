from flask import Blueprint, request, abort, make_response, Response
from ..db import db
from .route_utilities import validate_model, create_response_for_model
from ..models.video import Video

bp = Blueprint("video", __file__, url_prefix="/videos")

@bp.get("")
def get_all():
    query = db.select(Video).order_by(Video.id)
    videos = db.session.scalars(query)

    return [video.to_dict() for video in videos]

@bp.get("/<id>")
def get_one(id):
    video = validate_model(Video, id)
    return video.to_dict()

@bp.post("")
def create():
     return create_response_for_model(Video, request.get_json())

@bp.put("/<id>")
def update(id):
    video = validate_model(Video, id)
    try:
        video.update(request.get_json())
    except KeyError as error:
        response = {"details": f"Request body must include {error.args[0]}."}
        abort(make_response(response, 400))

    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.delete("/<id>")
def delete(id):
    video = validate_model(Video, id)

    db.session.delete(video)
    db.session.commit()

    return Response(status=204, mimetype="application/json")
