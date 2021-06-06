from models import User, Feedback, db
from app import app

db.drop_all()
db.create_all()

User.query.delete()

db.session.add(User(
    username = "Bob",
    password = "123456",
    email = "bob@bob.com",
    first_name = "Bob",
    last_name = "Alsobob"
))

db.session.commit()

db.session.add(Feedback(
    title = "test",
    content = "testtesttest",
    username = "Bob"
))

db.session.commit()