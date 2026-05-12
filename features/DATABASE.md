# Database Design

I will think to Make this as a ecommerce web so i will do trying to add thigns properly like the data i need to keep in a good way.

It will be `products` & `category` & `user`.


## How to use SQLITE DATABASE?
For sqlite i dont need to do anything special, in the create_engine() function i need to give the path of the database name only.


## How to use POSTGRES?
For postgres i need to start the service first and then come to use this.
suppose database name is: `rana_shop`
So in this case first i need to make sure this is exists and postgres is running.
```
sudo systemctl status postgresql
```
If it say not started or inactive then i need to run this service first with below command:
```
sudo systemctl start postgresql
```
If i dont start this service it will shows the connection refused.

### How about making a database in the postgres?
```terminal
rana@laptop:~$ sudo -iu postgres
[sudo] password for rana: 
postgres@laptop:~$ psql
psql (18.3 (Ubuntu 18.3-1.pgdg24.04+1))
Type "help" for help.

postgres=# 
postgres=# 
postgres=# create database rana_database owner rana;
CREATE DATABASE
postgres=# 
```

## Using Alembic
I will use alembic so that in future i can easily upgrade to new tables, columns and so on.

```
alembic init alembic
```
After running this upper i need to change some configuration to allow alembic make table's in my database.

```
alembic revision --autogenerate -m "initial migration first time"
```
This will generate the some files in the alembic/versions/*py file.
```
alembic upgrade head
```
This will do changes the structer of the database and from then i will able to add new data in the database.

then i will change the model in my code and do follow the upper things again.
then i will make sure to add this new model in the env.py or else in the `__init__.py`
if the `__init__.py` file is imported in the .env


## 📦 Products Table

- id_
- name
- category_id
- buy_price
- sell_price
- mrp
- stock_quantity
- updated_at -> i will store the posix int value here

---

## 📂 Categories Table

- id
- name
- description

---

## 🔗 Relationships

- One category → many products


## User Table
This is for storing user informations here for now i will make one table

- id_ 
- first_name
- middle_name
- last_name
- phone_no
- email_id


# My Database's Functions i will make:

CREATE:
- add one row
- add many row

READ:
- read one row by id_ ie primary_key
- read one row by a value of any column
- read range of row with offset and limit
- read all the row

UPDATE:
- update one row by finding its primary key


DELETE:
- delete one row
- delete some row