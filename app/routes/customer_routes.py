from flask import Blueprint, request, abort, make_response, Response
from ..db import db
from .route_utilities import validate_model, create_response_for_model
from ..models.customer import Customer

bp = Blueprint("customer", __file__, url_prefix="/customers")

@bp.get("")
def get_all():
    query = db.select(Customer).order_by(Customer.id)
    customers = db.session.scalars(query)

    return [customer.to_dict() for customer in customers]

@bp.get("/<id>")
def get_one(id):
    customer = validate_model(Customer, id)
    return customer.to_dict()

@bp.post("")
def create():
     return create_response_for_model(Customer, request.get_json())

@bp.put("/<id>")
def update(id):
    customer = validate_model(Customer, id)
    try:
        customer.update(request.get_json())
    except KeyError as error:
        response = {"details": f"Request body must include {error.args[0]}."}
        abort(make_response(response, 400))

    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.delete("/<id>")
def delete(id):
    customer = validate_model(Customer, id)

    db.session.delete(customer)
    db.session.commit()

    return Response(status=204, mimetype="application/json")
