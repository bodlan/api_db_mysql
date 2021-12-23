from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:bodlan123987@localhost/delivery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
ma=Marshmallow(app)

class customer(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))
    address=db.Column(db.String(100))
    email=db.Column(db.String(50))
    phone=db.Column(db.String(14))

    def __init__(self,name,address,email,phone):
        self.name=name
        self.address=address
        self.email=email
        self.phone=phone

class CustomerSchema(ma.Schema):
    class Meta:
        fields=("id","name","address","email","phone")


customer_schema=CustomerSchema()
customers_schema=CustomerSchema(many=True)

class CustomerManager(Resource):
    @staticmethod
    def get():
        try: id=request.args['id']
        except Exception as _: id=None
        if not id:
            Customers=customer.query.all()
            return jsonify(customers_schema.dump(Customers))
        Customer=customer.query.get(id)
        return jsonify(customer_schema.dump(Customer))
    @staticmethod
    def post():
        name=request.args['name']
        print("name:",name)
        address=request.args['address']
        email=request.args['email']
        phone=request.args['phone']
        Customer=customer(name, address, email, phone)
        db.session.add(Customer)
        db.session.commit()
        return jsonify({'Message':f'Customer {name} inserted'})
    @staticmethod
    def put():
        try:
            id=request.args['id']
        except Exception as _: id=None
        if not id:
            return jsonify({'Message':'Must provide the customer ID'})
        Customer=customer.query.get(id)
        if "name" in request.args:
            name=request.args['name']
            Customer.name = name
        if 'address' in request.args:
            address = request.args['address']
            Customer.address = address
        if 'email' in request.args:
            email = request.args['email']
            Customer.email = email
        if 'phone' in request.args:
            phone = request.args['phone']
            Customer.phone = phone
        db.session.commit()
        return jsonify({'Message':f'Customer with id={id} altered'})
    @staticmethod
    def delete():
        try: id=request.args['id']
        except Exception as _: id=None
        if not id:
            return jsonify({'Message':'Must provide ID'})
        Customer=customer.query.get(id)
        db.session.delete(Customer)
        db.session.commit()
        return jsonify({'Message':f'Customer {id} deleted'})

api.add_resource(CustomerManager,'/api/customers')
if __name__ == '__main__':
    app.run(debug=True)