from ..controllers import create_data_transactions,delete_transactions
from app import app
from flask import request, jsonify
import json

@app.route('/user/transactions', methods=['POST'])
def deposito():
    data = json.loads(request.data)
    
    return create_data_transactions(data)
@app.route('/user/transactions/<id>', methods=['DELETE'])
def delete(id):
    
    return delete_transactions(id)