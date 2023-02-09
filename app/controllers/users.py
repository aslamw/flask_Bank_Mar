#imports
import re
from flask import jsonify
from ..models.data_users.CRUD \
import create_data_user ,update_user, delete_user, user_by_data, exist_key

#utis
F_email = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')#format E-mail


#main
def create_user(data):
    
    #validation
    try:
        if not F_email.match(data["email"]) or len(data["cpf"]) != 11 or not data["name"].isalpha():
            return jsonify('invalid format'),400
        
        
        return jsonify(create_data_user(data)),201
    except :
        return jsonify('server error'),500
        

def get_by_id(id):
    if exist_key("id",id):
        if (data := user_by_data("id",id)):
            return jsonify(data),202
        else:
            return jsonify('Service Unavailable'),503
    return jsonify('invalid ID'),400

def put_user(id,data):
    
    if exist_key("id",id):
        if (data := update_user(id,data)):
            return jsonify(data),202
        else:
            return jsonify('Service Unavailable'),503
    return jsonify('invalid ID'),400
    
def del_user(id):
    if exist_key("id",id):
        if (data := delete_user(id)):
            return jsonify(data),202
        else:
            return jsonify('Service Unavailable'),503
    return jsonify('invalid ID'),400


def user_by_key(key,value):
    if exist_key(key,value):
        if (data := user_by_data(key,value)):
            return jsonify(data),202
        else:
            return jsonify('Service Unavailable'),503
    return jsonify(f'invalid {key}'),400
