import csv
from datetime import datetime
from app import db, create_app  # adjust based on your project structure
from app.models.customer import Customer  # adjust import path to where Customer model is defined

# Initialize Flask app and app context
app = create_app()
with app.app_context():
    # Optional: clear out existing data
    db.session.query(Customer).delete()

    # Load data from CSV
    with open('/Users/dehuihu/Documents/Ada_exercises/unit2/customers.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customer = Customer(
                id=int(row['id']),
                name=row['name'],
                postal_code=row['postal_code'],
                phone=row['phone_number'],
                register_at=row['register_at']
            )
            db.session.add(customer)

    # Commit all changes
    db.session.commit()
    print("Database seeded successfully.")
