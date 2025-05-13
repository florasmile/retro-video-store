import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from app.models.video import Video
from app.models.customer import Customer
from app.models.rental import Rental
from dotenv import load_dotenv
import os

load_dotenv()

VIDEO_TITLE = "A Brand New Video"
VIDEO_INVENTORY = 1
VIDEO_RELEASE_DATE = "01-01-2001"

CUSTOMER_NAME = "A Brand New Customer"
CUSTOMER_POSTAL_CODE = "12345"
CUSTOMER_PHONE = "123-123-1234"

RENTAL_DUE_DATE = "02-12-2008"

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_video(app):
    new_video = Video(
        title=VIDEO_TITLE, 
        release_date=VIDEO_RELEASE_DATE,
        total_inventory=VIDEO_INVENTORY,
        )
    db.session.add(new_video)
    db.session.commit()

@pytest.fixture
def second_video(app):
    new_video = Video(
        title="Video Two", 
        release_date="12-31-2000",
        total_inventory=1,
        )
    db.session.add(new_video)
    db.session.commit()

@pytest.fixture
def third_video(app):
    new_video = Video(
        title="Video Three", 
        release_date="01-02-2001",
        total_inventory=1,
        )
    db.session.add(new_video)
    db.session.commit()

@pytest.fixture
def five_copies_video(app):
    new_video = Video(
        title=VIDEO_TITLE, 
        release_date=VIDEO_RELEASE_DATE,
        total_inventory=5,
        )
    db.session.add(new_video)
    db.session.commit()

@pytest.fixture
def one_customer(app):
    new_customer = Customer(
        name=CUSTOMER_NAME,
        postal_code=CUSTOMER_POSTAL_CODE,
        phone=CUSTOMER_PHONE,
        register_at="01-01-2001"
    )
    db.session.add(new_customer)
    db.session.commit()

@pytest.fixture
def second_customer(app):
    new_customer = Customer(
        name="Second Customer",
        postal_code="12345",
        phone="234-234-2345",
        register_at="01-01-2001"
    )
    db.session.add(new_customer)
    db.session.commit()

@pytest.fixture
def third_customer(app):
    new_customer = Customer(
        name="Customer Three",
        postal_code= "12344",
        phone="000-000-0000",
        register_at="01-01-2001"
    )
    db.session.add(new_customer)
    db.session.commit()

@pytest.fixture
def one_checked_out_video(app, client, one_customer, one_video):
    new_rental = Rental(
        customer_id=1,
        video_id=1,
        due_date=RENTAL_DUE_DATE,
        status="RENTED"
    )

    db.session.add(new_rental)
    db.session.commit()

@pytest.fixture
def second_checked_out_video(app, client, one_customer, second_video):
    new_rental = Rental(
        customer_id=1,
        video_id=2,
        due_date=RENTAL_DUE_DATE,
        status="RENTED"
    )

    db.session.add(new_rental)
    db.session.commit()

@pytest.fixture
def third_checked_out_video(app, client, one_customer, third_video):
    new_rental = Rental(
        customer_id=1,
        video_id=3,
        due_date=RENTAL_DUE_DATE,
        status="RENTED"
    )

    db.session.add(new_rental)
    db.session.commit()

@pytest.fixture
def one_returned_video(app, client, one_customer, second_video):
    new_rental = Rental(
        customer_id=1,
        video_id=2,
        due_date=RENTAL_DUE_DATE,
        status="AVAILABLE"
    )

    db.session.add(new_rental)
    db.session.commit()

@pytest.fixture
def customer_one_video_three(app, client, one_customer, five_copies_video):
    new_rental = Rental(
        customer_id=1,
        video_id=1,
        due_date=RENTAL_DUE_DATE,
        status="AVAILABLE"
    )

    db.session.add(new_rental)
    db.session.commit()

@pytest.fixture
def customer_two_video_three(app, client, second_customer, five_copies_video):
    new_rental = Rental(
        customer_id=2,
        video_id=1,
        due_date=RENTAL_DUE_DATE,
        status="AVAILABLE"
    )

    db.session.add(new_rental)
    db.session.commit()

@pytest.fixture
def customer_three_video_three(app, client, third_customer, five_copies_video):
    new_rental = Rental(
        customer_id=3,
        video_id=1,
        due_date=RENTAL_DUE_DATE,
        status="AVAILABLE"
    )

    db.session.add(new_rental)
    db.session.commit()
