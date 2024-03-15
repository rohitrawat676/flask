from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)


# new_user = User(username='rohitrawat676', email='rohitrawat676@gmail.com')
# db.session.add(new_user)
# db.session.commit()

# users = User.query.all()
# for user in users:
#     print(user.username, user.email)

# user = User.query.filter_by(username='rohitrawat676').first()
# user.email = 'rohitrawat2089@example.com'
# db.session.commit()

# user = User.query.filter_by(username='rohitrawat676').first()
# db.session.delete(user)
# db.session.commit()
