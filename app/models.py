from  .import db
#user =
class User(db.model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64),nullable=False,unique=True)
    email=db.Column(db.String(120),nullable=False,unique=True)
    password=db.Column(db.String(128),nullable=False)
    posts=db.relationship('Post',backref='author',lazy=True)