# Starter Template for Flask
```
from flask import Flask

app=Flask(__name__)

@app.route('/')
def helloWorld():
    return '''<h1>Hello but Bigger</h1>'''

if __name__=='__main__':
    app.run(debug=True)
```


# Making varaibles pass in the routes
```
@app.route('/about/<username>')

we have to pass the username in the function for further coding

```

# To avoid the Not responding page and to set a default page
```
@app.route('/')
@app.route('/home')
def home_page():
   return render_template('home.html')
```

# To pass the variable in the templates
```
def market_page():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]

    return render_template('market.html', items=items)
```
# Jinja Techniques
```
For applying logic in page use {% %}

For loop synatax:
   { % for item in items%}
    <tr>
        <th scope="row">1</th>
            <td>Mark</td>
            <td>Otto</td>
            <td>@mdo</td>
    </tr>
    {% endfor %}
```
# Template Inheritance
```
we have to put all the repetative codes in the base.html

base.html:
 <title>
    {% block title%}

    {% endblock%}
</title>

    
      {% block content %}
      
      {% endblock %}

      put like these blocks in jinja wherever you want to replace the code.

in the child class:
this kind of boiler plate should be there if you are using template literals

    {% extends 'base.html'%}

        {% block title%}
        Market Page
        {% endblock%}
```
# Creating a database using SQLAlchemy
While using python to create a database that database is called Model
where classes are used to create the table 
```
list of all common SQLAlchemy data types:

1. Integer                  
2. BigInteger
3. SmallInteger
4. Numeric
5. Float
6. Boolean
7. String
8. Text
9. Unicode
10. UnicodeText
11. CHAR
12. NCHAR
13. VARCHAR
14. NVARCHAR
15. Date
16. Time
17. DateTime
18. Interval
19. Enum
20. LargeBinary
21. Binary
22. CLOB
23. DECIMAL

text list of common arguments for `db.Column`:

1. type_
2. primary_key
3. unique
4. index
5. nullable
6. default
7. server_default
8. server_onupdate
9. autoincrement
10. comment
11. doc
12. onupdate
13. foreign_key
14. primary_key_constraint
15. unique_constraint
16. index_constraint
```

# There is a important part i.e packaging of python files
Method to package
Stricty follow the structure
```
Files 

your_project/
│
├── market/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── home.html
│   │   └── market.html
│
└── run.py

```
```
market/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market_data.db'
db = SQLAlchemy(app)

from market import routes  # Import routes at the end to avoid circular imports

```
```
market/models.py

from market import db

class Items(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False)

    def __repr__(self):
        return f'Item {self.name}'
```
```
market/routes.py

from flask import render_template
from market import app
from market.models import Items

@app.route('/')
@app.route('/home')
def home_page():
   return render_template('home.html')

@app.route('/market')
def market_page():
    items = Items.query.all()
    return render_template('market.html', items=items)

```
```
run.py

from market import app

if __name__ == '__main__':
    app.run(debug=True)

```