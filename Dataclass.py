from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import query
from app import db

#データベースのクラス
class Data(db.Model):
    __tablename__ = 'Data'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    classification = db.Column(db.Text())
    author = db.Column(db.Text())
    title = db.Column(db.Text())
    contents = db.Column(db.Text())
    def __init__(self,classification,author,title,contents):
      self.classification =  classification
      self.author = author
      self.title = title
      self.contents = contents
      

def add(new_post):
  db.session.add(new_post)
  db.session.commit()

def delete(id):
    post=Data.query.get(id)
    db.session.delete(post)
    db.session.commit()