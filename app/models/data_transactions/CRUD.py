from . import db
from sqlalchemy.orm import Session
from sqlalchemy import inspect
from ..data_users.db import Users
from ..data_users.CRUD import user_by_data,update_count_user

session = Session(db.engine)

def object_as_dict(obj):
    """
        conver os dados para dict
    """
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

def create_data_transactions(data):
    
    value_count = user_by_data('id',data["id_user"])
    value_count_T = user_by_data('id',data["id_user_T"])
    
    match data["type_transaction"]:
        
        case 'deposit':
            
            update_count_user(data["id_user"],value_count['count']- data['value'])
            
        case 'transfer':
            oi = (int(value_count_T['count'])-int(data['value']))
            update_count_user(data["id_user_T"],oi)
            
            print(f"data : {type(oi)},{type(value_count['count'])},{type(data['value'])}")
            update_count_user(data["id_user"],value_count['count'] + data['value'])
            
        case 'withdraw':
            
            update_count_user(data["id_user"],(int(value_count["count"])-int(data["value"])))
            
            
    data = db.Transactions(
                id_user = data["id_user"],
                id_user_T = data["id_user"],
                type_transaction = data["type_transaction"],
                value = data["value"]
            )
    
    session.add_all([data])
    session.commit()
    
    return 'ok'

def delete_user(id):

    session.query(db.Transactions). \
    filter(db.Transactions.id == id).delete()
    
    session.commit()
    
    return 'ok'