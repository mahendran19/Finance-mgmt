# Create your models here.
from datetime import datetime
from pony.orm import *


db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str, 250)
    password = Required(str, 250)
    password = Required(str, 250)
    firstname = Required(str, 250)
    lastname = Required(str, 64)
    Email = Required(str, 255)
    gender = Required(str, 255)
    incomes = Set('Income')
    expenses = Set('Expense')


class Income(db.Entity):
    id = PrimaryKey(int, auto=True)
    mode = Required(str)
    amount = Required(float)
    user = Required(User)
    addedon = Required(datetime)


class Expense(db.Entity):
    id = PrimaryKey(int, auto=True)
    amount = Required(float)
    mode = Required(str)
    user = Required(User)
    addon = Required(datetime)



db.generate_mapping()




