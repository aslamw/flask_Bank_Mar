from app import app
from ..controllers \
import create_user, get_by_id, put_user, del_user, user_by_key
from flask import jsonify, request
import json

@app.route('/', methods=['GET'])
def root():
    return jsonify({'message':'Bank Mar ok!'}),200

@app.route('/user/create', methods=['POST'])
def route_create_user():
    data = json.loads(request.data),201
    
    return create_user(data[0])

@app.route('/user/<id>',methods=['GET'])
def route_user_id(id):
    return get_by_id(id)

@app.route('/user/update/<id>', methods=['PUT'])
def route_update_user(id):
    data = json.loads(request.data)
    
    return jsonify({'data':put_user(id,data)})

@app.route('/user/delete/<id>', methods=['DELETE'])
def route_delete_user(id):
    
    return jsonify({'menssage': del_user(id)}) ,200

@app.route('/user/key', methods=['POST'])
def user_key():
    data = json.loads(request.data)
    
    return user_by_key(data['key'],data['value'])