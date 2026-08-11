from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 1. Database Configuration
# Syntax: mysql://username:password@hostname/database_name
# 'Bharat@1297'  or 'Bharat%401297' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Bharat%401297@localhost/college'


# ADD THIS LINE HERE:
app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the ORM
db = SQLAlchemy(app)



# 2. Database Model Definition (Table)
class Driver(db.Model):
    __tablename__ = 'drivers'  # Specifies the table name explicitly

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # Helper method to convert database objects to dictionary format
    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age}


# 3. Create Tables automatically inside the database
with app.app_context():
    db.create_all()


# 4. OPERATION: CREATE (Insert a new driver)
@app.route('/driver', methods=['POST'])
def create_driver():
    data = request.get_json()

    # Form the database object
    new_driver = Driver(name=data['name'], age=data['age'])
    

    db.session.add(new_driver)  # Stage the record
    db.session.commit()  # Save changes to MySQL

    return jsonify({"message": "Driver created successfully!", "driver": new_driver.to_dict()}), 201


# 5. OPERATION: READ (Get all drivers)
@app.route('/drivers', methods=['GET'])
def get_drivers():
    # Equivalent to: SELECT * FROM drivers;
    all_drivers = Driver.query.all()
    
    drivers_with_age_25 = Driver.query.filter_by(age=25).all()

    # Convert the records into JSON format
    drivers_list = [driver.to_dict() for driver in all_drivers]
    filtered_list= [driver.to_dict() for driver in drivers_with_age_25]
    return jsonify({
        "all_drivers": drivers_list,
        "filtered_drivers": filtered_list}), 200


# 6. OPERATION: UPDATE (Modify an existing driver by ID)
@app.route('/driver/<int:id>', methods=['PUT'])
def update_driver(id):
    # Find the driver or return a 404 error if not found
    driver = Driver.query.get_or_404(id)
    data = request.get_json()

    # Update fields if they exist in the incoming request
    if 'name' in data:
        driver.name = data['name']
    if 'age' in data:
        driver.age = data['age']

    db.session.commit()  # Save the updates to MySQL
    return jsonify({"message": "Driver updated successfully!", "driver": driver.to_dict()}), 200


# 7. OPERATION: DELETE (Remove a driver by ID)
@app.route('/driver/<int:id>', methods=['DELETE'])
def delete_driver(id):
    # Find the driver or return a 404 error if not found
    driver = Driver.query.get_or_404(id)

    db.session.delete(driver)  # Stage for removal
    db.session.commit()  # Permanently remove from MySQL

    return jsonify({"message": f"Driver with ID {id} has been deleted."}), 200


if __name__ == '__main__':
    app.run(debug=True)
