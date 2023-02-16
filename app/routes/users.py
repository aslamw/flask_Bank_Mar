from app import app

from ..controllers \
import create_user, get_by_id, put_user, del_user, user_by_key, login, token_required, \
verify_and_decode_jwt,create_jwt

from flask import jsonify, request
import json

#utils
def id_auth():
    token = request.headers.get('autho')
    return verify_and_decode_jwt(token)

#routes

@app.route('/', methods=['GET'])
def root():
    return jsonify({'message':'Bank Mar ok!'}),200

@app.route('/user/create', methods=['POST'])
def route_create_user():
    data = json.loads(request.data)
    
    return create_user(data)

@app.route('/user/login', methods=['POST'])
def route_login_user():
    data = json.loads(request.data)
    
    return login(data)

@app.route('/user',methods=['GET'])
@token_required
def route_user_id():
    data =  id_auth()
    if not data:
       return jsonify('	Unauthorized'),401
    return get_by_id(data['id'])

@app.route('/user/update/', methods=['PUT'])
@token_required
def route_update_user():
    data = json.loads(request.data)
    data_id =  id_auth()
    if not data_id:
       return jsonify('	Unauthorized'),401
    
    return put_user(data_id["id"],data)

@app.route('/user/delete', methods=['DELETE'])
@token_required
def route_delete_user():
    data =  id_auth()
    if not data:
       return jsonify('	Unauthorized'),401
    
    return del_user(data["id"])

@app.route('/user/key', methods=['POST'])
@token_required
def user_key():
    data = json.loads(request.data)
    
    return user_by_key(data['key'],data['value'])