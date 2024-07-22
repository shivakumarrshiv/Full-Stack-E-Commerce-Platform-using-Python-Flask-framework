from market import db,login_manager
from market import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Items', backref='owned_user', lazy=True)

    @property
    def put_comma(self):
        if len(str(self.budget))>=4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f'{self.budget}$'

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text):
        self.password_hash = bcrypt.generate_password_hash(plain_text).decode('utf-8')

    def check_password(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)

    def can_purchase(self,item_purchased):
        return self.budget >= item_purchased.price

    def can_sell(self,want_to_sell):
        return want_to_sell in self.items

    # def is_active(self):
    #     return self.active

    # def get_id(self):
    #     return self.id

    # def is_authenticated(self):
    #     return True

    # def is_anonymous(self):
    #     return False

class Items(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'

    def buy(self,user):
         self.owner=user.id
         user.budget -= self.price
         db.session.commit()

    def sell(self,user1):
        self.owner=None
        user1.budget += self.price
        db.session.commit()