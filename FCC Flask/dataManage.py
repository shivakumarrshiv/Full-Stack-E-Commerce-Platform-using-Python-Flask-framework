from market.models import db,User,Items
from market import app
import os

with app.app_context():
    # db.create_all()
    # u1=User(username='arun',email_address='arun@gmail.com',password_hash='123',budget=2334)
    # db.session.add(u1)
    # db.session.commit()
    # u2=User(username='varun',email_address='varun@gmail.com',password_hash='21323',budget=12334)
    # db.session.add(u2)
    # db.session.commit()
    # i1=Items(name='Iphone10',price=300,barcode='342564785362',description='very good')
    # db.session.add(i1)
    # db.session.commit()
    # i2=Items(name='Laptop Asus',price=1500,barcode='3425667571234',description='very good laptop')
    # db.session.add(i2)
    # db.session.commit()
    # item1=Items.query.filter_by(name='Iphone10').first()
    # # print(item1)
    # item1.owner=User.query.filter_by(username='arun').first().id
    # # db.session.add(item1)
    # # # db.session.commit()
    # # print(item1.owner)
    # i=Items.query.filter_by(name='Iphone10').first()
    # print(i.owned_user)
    i3 = Items(name='Google Pixel 5', price=600, barcode='987654321098', description='excellent camera')
    i4 = Items(name='OnePlus 8', price=550, barcode='234567890123', description='fast performance')
    i5 = Items(name='Sony Xperia 1', price=650, barcode='345678901234', description='stunning display')
    i6 = Items(name='Nokia 8.3', price=400, barcode='456789012345', description='solid build')
    i7 = Items(name='Huawei P30 Pro', price=500, barcode='567890123456', description='great battery life')
    i8 = Items(name='LG V60 ThinQ', price=450, barcode='678901234567', description='dual screen')
    i9 = Items(name='Xiaomi Mi 10', price=480, barcode='789012345678', description='impressive specs')
    i10 =Items(name='Motorola Edge Plus', price=620, barcode='890123456789', description='sleek design')

    db.session.add(i3)
    db.session.add(i4)
    db.session.add(i5)
    db.session.add(i6)
    db.session.add(i7)
    db.session.add(i8)
    db.session.add(i9)
    db.session.add(i10)
    db.session.commit()

    
