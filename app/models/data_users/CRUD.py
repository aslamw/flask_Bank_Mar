from . import db
from sqlalchemy.orm import Session
from sqlalchemy import inspect, exists

session = Session(db.engine)

#utils
def exist_key(key,value):
    
    data = False
    match key:
        
        case "email":
            data = session.query(db.Users).filter(db.Users.email == value).count()
        case "cpf":
            data = session.query(db.Users).filter(db.Users.cpf == value).count()
        case "id":
            data = session.query(db.Users).filter(db.Users.id == value).count()
        case "name":
            data = session.query(db.Users).filter(db.Users.name == value).count()
        case _:
            return data

    session.commit()
    
    return data
    
def object_as_dict(obj):
    """
        conver os dados para dict
    """
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

#main
def create_data_user(data):
    
    data = db.Users(
        name=data["name"],
        cpf = data["cpf"],
        email = data["email"],
        password = data["password"],
        count = 0 
    )
    
    session.add_all([data])
    session.commit()
    
    return 'ok'

def user_by_data(key,value):
    
    """ data = session.query(db.Users).filter(db.Users.id == 1)
    session.query(data.exists()) """
    
    
    data = False
    match key:
        
        case "email":
            data = object_as_dict( session.query(db.Users).filter(db.Users.email == value).one() )
        case "cpf":
            data = object_as_dict( session.query(db.Users).filter(db.Users.cpf == value).one() )
        case "id":
                data = object_as_dict( session.query(db.Users).filter(db.Users.id == value).one() )
        case "name":
            data = object_as_dict( session.query(db.Users).filter(db.Users.name == value).one() )
            
            
    session.commit()
    
    return data

def update_user(id,data_up):

    session.query(db.Users). \
    filter(db.Users.id == id) \
    .update({'name':data_up['name'],'email':data_up['email'], 'password':data_up['password']})
    
    session.commit()
    
    return 'ok'
def update_count_user(id,data_up):

    session.query(db.Users). \
    filter(db.Users.id == id) \
    .update({'count':data_up})
    
    session.commit()
    
    return 'ok'
    
def delete_user(id):

    session.query(db.Users). \
    filter(db.Users.id == id).delete()
    
    session.commit()
    
    return 'ok'
