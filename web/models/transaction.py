from app import db


class Transaction(db.Model):

    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float, nullable=False)
    recurring = db.Column(db.DateTime, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    def __init__(self, amount, recurring, category_id, person_id):
        self.amount = amount
        self.recurring = recurring
        self.category_id = category_id
        self.person_id = person_id
