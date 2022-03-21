from sqlalchemy import insert, select
from db import Base, engine, execute
from models import User, Address

Base.metadata.create_all(engine)


def insert_one():
    query = insert(User).values(
        name = 'Johnny',
        fullname = 'Carter',
        gender = 'male',
        age = 31
    )
    execute(query)
    #with engine.connect() as conn:
    #    conn.execute(query)
insert_one()

def insert_many():
    query = insert(User)
    execute(query, [{
            'name':'Ann',
            'fullname':'Anna Karenina',
            'gender': 'female',
            'age': 33
        }, {
            'name': 'Kolya',
            'fullname': 'Nikolay Baskov',
            'gender' : 'male',
            'age' : 45
        }])
    

insert_many()

def insert_five_people():
    query = insert(User)
    execute(query,[{
            'name': 'Bob',
            'fullname': 'Bob Morley',
            'gender': 'male',
            'age': 37
    },{
            'name': 'Hugh',
            'fullname': 'Hugh Grant',
            'gender': 'male',
            'age': 61
    },{
            'name': 'Lory',
            'fullname':'Lory Harvey',
            'gender': 'female',
            'age': 25
    },{
            'name': 'Law',
            'fullname': 'Law Jude',
            'gender': 'male',
            'age': 49
    },{
            'name': 'Anthony', 
            'fullname':'Anthony Hopkins',
            'gender': 'male',
            'age': 84 
    }]) 


    # with engine.connect() as conn:
    #     query = select(User)
    #     result = conn.execute(query)
    #     for row in result:
    #         print(dict(row))
insert_five_people()

with engine.connect() as conn:
        query = (
            select(User.name,User.gender,User.age)
            .where(User.gender == 'male')
            .where(User.name.like('L%')| User.name.like('H%')
            )
            .order_by(User.age.desc())
            .limit(3)
        )

        result = conn.execute(query)
        for row in result:
            print(dict(row))