from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///joins.db"
db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))



class Purchase(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    customer_id = db.Column(db.Integer,db.ForeignKey("customer.id"))#here see customer is small ,even though class name is capital
    price = db.Column(db.Integer)


db.create_all()
'''
#just for adding data into the tables
import random

for i in range(5):
    db.session.add(Customer(name = random.choice(["Krishna","RadhaRani","Prabhupad","Radhanath Swami"])))
    db.session.commit()

for i in range(10):
    db.session.add(Purchase(customer_id = random.randrange(1,5,1), price = random.randrange(1000,2000,50)))
    db.session.commit()
'''

'''
Retreival checking , just trying to print the data in db once inserted

results = db.session.query(Customer).all()
# print(result.id,result.name)#AttributeError: 'list' object has no attribute 'id'
# ".all" returns list,so
for result in results:
    print(result.id,result.name)


result = db.session.query(Customer.name).all()
print(result)

results = db.session.query(Purchase).all()
# print(result.id,result.name)#AttributeError: 'list' object has no attribute 'id'
# ".all" returns list,so

for result in results:
    print(result.id,result.customer_id,result.price)
'''

#in sql how u do joins is
# select * from Customer left join Purchase on customer.id = purchase.customer_id;

'''
# results = db.session.query(Purchase).outerjoin(Purchase).all()
# sqlalchemy.exc.InvalidRequestError: Don't know how to join to <Mapper at 0x7f45bf0e8a60; 
# Purchase>. Please use the .select_from() method to establish an explicit left side, as well as 
# providing an explicit ON clause if not present already to help resolve the ambiguity.
'''

result = db.session.query(Purchase).select_from(Customer).outerjoin(Purchase).filter_by(price=1550).all()
print(result[0].price,result[0].customer_id)#1550 1


result_without_attributes = db.session.query(Customer,Purchase).join(Purchase).all()
# results = db.session.query(Customer.name,Purchase.customer_id).join(Purchase).all()
results = db.session.query(Customer.name,Purchase.customer_id,Purchase.price).join(Purchase, Customer.id == Purchase.customer_id).all()
for result in results:
    print(result)
'''
('RadhaRani', 3, 1750)
('Prabhupad', 2, 1000)
('RadhaRani', 1, 1450)
('Radhanath Swami', 4, 1650)
('RadhaRani', 3, 1900)
('RadhaRani', 1, 1200)
('RadhaRani', 3, 1750)
('Prabhupad', 2, 1900)
('RadhaRani', 1, 1400)
('RadhaRani', 1, 1550)


'''
results = db.session.query(Purchase.customer_id,Purchase.price).join(Customer).all()
for result in results:
    print(result)
'''
(3, 1750)
(2, 1000)
(1, 1450)
(4, 1650)
(3, 1900)
(1, 1200)
(3, 1750)
(2, 1900)
(1, 1400)
(1, 1550)
'''

'''
#Conclusion
Customer join Purchase
Purchase join Customer both are same since simple join na
'''


'''
# just trying to parse this output without attributes
for out in result_without_attributes:
    # print(out)
    if out[1]:
        print(out[0].name,out[1].customer_id,out[1].price)

RadhaRani 3 1750
Prabhupad 2 1000
RadhaRani 1 1450
Radhanath Swami 4 1650
RadhaRani 3 1900
RadhaRani 1 1200
RadhaRani 3 1750
Prabhupad 2 1900
RadhaRani 1 1400
RadhaRani 1 1550
'''






results_outer_join = db.session.query(Customer.name,Purchase.customer_id,Purchase.price).outerjoin(Purchase, Customer.id == Purchase.customer_id).all()
for res in results_outer_join:
    print(res)

print("#"*40)
results_outer_join = db.session.query(Customer.name,Purchase.customer_id,Purchase.price).outerjoin(Purchase).all()
for res in results_outer_join:
    print(res)
'''('RadhaRani', 1, 1200)
('RadhaRani', 1, 1400)
('RadhaRani', 1, 1450)
('RadhaRani', 1, 1550)
('Prabhupad', 2, 1000)
('Prabhupad', 2, 1900)
('RadhaRani', 3, 1750)
('RadhaRani', 3, 1750)
('RadhaRani', 3, 1900)
('Radhanath Swami', 4, 1650)
('RadhaRani', None, None)
########################################
('RadhaRani', 1, 1200)
('RadhaRani', 1, 1400)
('RadhaRani', 1, 1450)
('RadhaRani', 1, 1550)
('Prabhupad', 2, 1000)
('Prabhupad', 2, 1900)
('RadhaRani', 3, 1750)
('RadhaRani', 3, 1750)
('RadhaRani', 3, 1900)
('Radhanath Swami', 4, 1650)
('RadhaRani', None, None)
'''
print("@"*40)

results = db.session.query(Customer.name,Purchase.customer_id,Purchase.price).outerjoin(Customer).all()
for result in results:
    print(result)
'''('RadhaRani', 3, 1750)
('Prabhupad', 2, 1000)
('RadhaRani', 1, 1450)
('Radhanath Swami', 4, 1650)
('RadhaRani', 3, 1900)
('RadhaRani', 1, 1200)
('RadhaRani', 3, 1750)
('Prabhupad', 2, 1900)
('RadhaRani', 1, 1400)
('RadhaRani', 1, 1550)
'''

# results = db.session.query(Customer.name,Purchase.customer_id,Purchase.price).outerjoin(Customer).filter_by(price=1550).all()
# sqlalchemy.exc.InvalidRequestError: Entity namespace for "mapped class Customer->customer" has no property "price"

results = db.session.query(Customer.name,Purchase.customer_id,Purchase.price).outerjoin(Customer).filter(Purchase.price==1550).all()
print(results)#[('RadhaRani', 1, 1550)]



# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------

# Group by
#to use aggregate functions u have to use db.func.function_name as shown below
group_results = db.session.query(Customer.name,db.func.count(Purchase.customer_id),db.func.sum(Purchase.price)).outerjoin(Purchase).group_by(Customer.name).all()
print(group_results)

group_results = db.session.query(Customer.name,db.func.count(Purchase.customer_id),db.func.sum(Purchase.price)).outerjoin(Purchase).group_by(Customer.name).filter(Customer.name=="RadhaRani").all()
print(group_results)#[('RadhaRani', 7, 11000)]


if __name__ == "__main__":
    app.run(debug=True)


