from database import db
from typing import List


class MasterKosen(db.Model):

    __tablename__ = 'm_kosen'

    id = db.Column(db.Integer, primary_key=True)
    sub_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    postal_code = db.Column(db.Text(7))
    address = db.Column(db.Text())

    @staticmethod
    def get_school_list() -> List["MasterKosen"]:
        return MasterKosen.query.filter_by(sub_id=0).all()
