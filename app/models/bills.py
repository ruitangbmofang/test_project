from app.models import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    mobile = db.Column(db.String(20))
    address = db.Column(db.String(50), nullable=True)

    def __init__(self, name, mobile, address=None):
        self.name = name
        self.mobile = mobile
        self.address = address

    # def __repr__(self):
    #     return [self.name, self.mobile, self.address]


class Bills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    custom_id = db.Column(db.Integer)
    goods = db.Column(db.String(50))
    pay_status = db.Column(db.Integer, default=0)
    delivery_status = db.Column(db.Integer, default=0)
    open_time = db.Column(db.DATETIME)
    close_time = db.Column(db.DATETIME)

    def __init__(self, custom_id, goods):
        self.goods = goods
        self.custom_id = custom_id


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    goods_content = db.Column(db.String(200), nullable=True)
    colour = db.Column(db.String(20), nullable=True)
    unit_price = db.Column(db.Float)
    num = db.Column(db.Integer)
    type = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Integer, default=0)
    bill_id = db.Column(db.Integer, nullable=True)

    def __init__(self, name, goods_content, colour, unit_price, num, type, status, bill_id):
        self.name = name
        self.goods_content = goods_content
        self.colour = colour
        self.unit_price = unit_price
        self.num = num
        self.type = type
        self.status = status
        self.bill_id = bill_id


    def __repr__(self):
        return str([self.id, self.name, self.goods_content, self.colour,self.unit_price, self.num, self.type, self.status, self.bill_id])