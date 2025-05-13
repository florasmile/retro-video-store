from flask import Blueprint, request, Response, abort, make_response
from ..db import db
from ..models.customer import Customer
from .route_utilities import validate_model, create_response_for_model, update_model

bp = Blueprint("customers", __name__, url_prefix="/customers")

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
def create_one():
    return create_response_for_model(Customer, request.get_json())

@bp.put("/<id>")
def update_one(id):
    customer = validate_model(Customer, id)

    return update_model(customer, request.get_json())

@bp.delete("/<id>")
def delete_one(id):
    customer = validate_model(Customer, id)

    db.session.delete(customer)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

  
