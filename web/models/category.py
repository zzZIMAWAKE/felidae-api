from app import db


class Category(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    def __init__(self, name, person_id, parent_id):
        self.name = name
        self.person_id = person_id
        self.parent_id = parent_id