from flask import Blueprint, request, Response, abort, make_response
from ..db import db
from ..models.video import Video
from .route_utilities import validate_model, create_response_for_model, update_model

bp = Blueprint("videos", __name__, url_prefix="/videos")

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
def create_one():
    return create_response_for_model(Video, request.get_json())

@bp.put("/<id>")
def update_one(id):
    video = validate_model(Video, id)

    return update_model(video, request.get_json())

@bp.delete("/<id>")
def delete_one(id):
    video = validate_model(Video, id)

    db.session.delete(video)
    db.session.commit()

    return Response(status=204, mimetype="application/json")