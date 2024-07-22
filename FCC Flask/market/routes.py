from market import app
from flask import render_template,url_for,redirect,flash,request
from market.models import Items,User
from market.forms import RegistrationForm,LoginForm,PurchaseForm,SellForm
from market import db
from flask_login import login_user,logout_user,login_required,current_user

@app.route('/')
@app.route('/home')
def home_page():
   return render_template('home.html')

@app.route('/market', methods=['GET','POST'])
@login_required
def market_page():
    purchase_form=PurchaseForm()

    if request.method=='POST':
      p_item=request.form.get('purchased_item')
      p_item_obj=Items.query.filter_by(name=p_item).first()

      if p_item_obj:
         if current_user.can_purchase(p_item_obj):
            p_item_obj.buy(current_user)
            flash(f'Congratulations you have purchased {p_item_obj.name} for {p_item_obj.price}$', category='success')
         else:
            flash(f'Insufficient Balnace sorry you cannot buy the item', category='danger')

      

      sold_item=request.form.get('sold_item')
      s_item_obj=Items.query.filter_by(name=sold_item).first()

      if s_item_obj:
         if current_user.can_sell(s_item_obj):
            s_item_obj.sell(current_user)
            flash(f'Congratulations you have sold  {s_item_obj.name} for {s_item_obj.price}$', category='danger')
         else:
            flash(f'Congratulations you have purchased {s_item_obj} for {s_item_obj.price}$', category='success')

      return redirect(url_for('market_page'))

    if request.method=='GET':  
      owned_item=Items.query.filter_by(owner=current_user.id)
      selling_form=SellForm()
      items = Items.query.filter_by(owner=None)
      return render_template('market.html', items=items,purchase_form=purchase_form,owned_item=owned_item,selling_form=selling_form)

@app.route('/register', methods=['GET','POST'])
def register_page():
   form=RegistrationForm()
   if form.validate_on_submit():
      user_data=User(username=form.username.data,
                     email_address=form.email_address.data,
                     password=form.password1.data)

      db.session.add(user_data)
      db.session.commit()
      login_user(user_data)
      flash(f'You have succesfully created the account as {user_data.username}', category='success')
      return redirect(url_for('market_page'))

   if form.errors !={}:
      for error_msg in form.errors.values():
         flash(f'There is a error while creating the user {error_msg}',category='danger')

   return render_template('registration.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
   form= LoginForm()
   if form.validate_on_submit():
      user_attempted=User.query.filter_by(username=form.username.data).first()

      if user_attempted and user_attempted.check_password(form.password.data):
            login_user(user_attempted)
            flash(f'Successfully logged in as {user_attempted.username}',category='success')
            return redirect(url_for('market_page'))

      else:
         flash('Username and Password are incorrect!!',category='danger')


   return render_template('login.html',form=form)

@app.route('/logout')
def logout_page():
   logout_user()
   flash('You have been successfully logged out', category='info')
   return redirect(url_for('home_page'))




   