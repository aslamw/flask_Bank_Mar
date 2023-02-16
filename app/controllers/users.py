#imports
import re, jwt, os, datetime
from flask import jsonify
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.data_users.CRUD \
import create_data_user ,update_user, delete_user, user_by_data, exist_key
from.service import create_jwt

#utils
load_dotenv()
F_email = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')#format E-mail


#main
def create_user(data):
    
    #validation
    try:
        if not F_email.match(data["email"]) or len(data["cpf"]) != 11 or not data["name"].isalpha():
            return jsonify('invalid format'),400
        
        data["password"] = generate_password_hash(data["password"])
        
        return jsonify(create_data_user(data)),201
    except :
        return jsonify('server error'),500
        
def login(data):
    #try:
    if not F_email.match(data["email"]):
        return jsonify('invalid format'),400
    
    if not exist_key('email',data["email"]):
        return jsonify('not exist email'),401
    
    data_user = user_by_data('email',data["email"])
    
    if not check_password_hash(data_user["password"],data["password"]):
        return jsonify('invalid password'),401
    #jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    
    token = {
        'id':data_user["id"],
        'exp': (date_jwt := (datetime.datetime.now() + datetime.timedelta(minutes=5)).timestamp())}
    
    
    return jsonify({'message':'validated sucessfully', 'token': create_jwt(token), 'exp':date_jwt} ), 200
    #except :
    #    return jsonify('server error'),500
    
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
            return jsonify({'data':data}),202
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
