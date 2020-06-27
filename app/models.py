from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), unique=True, nullable=False)
    req_short = db.Column(db.Text(), nullable=False)
    req_full = db.Column(db.Text(), nullable=False)
    benefits_short = db.Column(db.Text(), nullable=False)
    benefits_full = db.Column(db.Text(), nullable=False)
    application = db.Column(db.Text(), nullable=False)
    website = db.Column(db.String(250), nullable=False)
    # PLAN KEYWORDS
    # kw1 = Childcare
    # kw2 = Disability Aid
    # kw3 = Elderly Aid
    # kw4 = HDB
    # kw5 = Healthcare
    # kw6 = Low Income
    kw1 = db.Column(db.Boolean(), nullable=False)
    kw2 = db.Column(db.Boolean(), nullable=False)
    kw3 = db.Column(db.Boolean(), nullable=False)
    kw4 = db.Column(db.Boolean(), nullable=False)
    kw5 = db.Column(db.Boolean(), nullable=False)
    kw6 = db.Column(db.Boolean(), nullable=False)

    def __repr__(self):
        return f"Plan Name: {self.name}"
