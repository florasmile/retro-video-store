from flask import Blueprint, request, abort, make_response
from ..models.customer import Customer
from ..models.video import Video
from ..models.rental import Rental
from .route_utilities import validate_model, create_response_for_model
from ..db import db
from sqlalchemy import and_

bp = Blueprint("rentals", __name__, url_prefix="/rentals")

@bp.post("/check-out")
def rental_check_out():
    request_body = request.get_json()
    try:
        customer_id = request_body["customer_id"]
        video_id = request_body["video_id"]
    except KeyError as err:
        invalid = {"message": f"missing {err.args[0]} in request body"}
        abort(make_response(invalid, 400))
    
    customer = validate_model(Customer, customer_id)
    video = validate_model(Video, video_id)

    # get available inventory
    query = db.select(Rental).where(
        and_(
            Rental.video_id == video_id,
            Rental.status == "RENTED"
        )
    )
    rentals = db.session.scalars(query).all()
    videos_checked_out_count = len(rentals)
    available_inventory = video.total_inventory - videos_checked_out_count

    if available_inventory == 0:
        response = {"message": "Could not perform checkout"}
        abort(make_response(response, 400))
        # update total_inventory
    # create rental record and commit to db

    rental = Rental.from_dict(request_body)
    db.session.add(rental)
    db.session.commit()

    return {
        "customer_id": customer.id,
        "video_id": video.id,
        "due_date": rental.due_date,
        "videos_checked_out_count": videos_checked_out_count + 1,
        "available_inventory": available_inventory - 1
    }


# @bp.post("/check-in")
# def rental_check_in():

