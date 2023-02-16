from functools import wraps
import os, hmac, hashlib, base64, json, datetime
from flask import request, jsonify
from dotenv import load_dotenv

load_dotenv()
secret_key = os.environ["SECRET_KEY"]

def create_jwt(payload):
    payload = json.dumps(payload).encode()
    header = json.dumps({
        'typ': 'JWT',
        'alg': 'HS256'
    }).encode()
    b64_header = base64.urlsafe_b64encode(header).decode()
    b64_payload = base64.urlsafe_b64encode(payload).decode()
    signature = hmac.new(
        key=secret_key.encode(),
        msg=f'{b64_header}.{b64_payload}'.encode(),
        digestmod=hashlib.sha256
    ).digest()
    jwt = f'{b64_header}.{b64_payload}.{base64.urlsafe_b64encode(signature).decode()}'
    return jwt

def verify_and_decode_jwt(jwt):
    
    
    if not jwt:
        return False
    
    b64_header, b64_payload, b64_signature = jwt.split('.')
    b64_signature_checker = base64.urlsafe_b64encode(
        hmac.new(
            key=secret_key.encode(),
            msg=f'{b64_header}.{b64_payload}'.encode(),
            digestmod=hashlib.sha256
        ).digest()
    ).decode()

    # payload extraido antes para checar o campo 'exp'
    payload = json.loads(base64.urlsafe_b64decode(b64_payload))
    unix_time_now = datetime.datetime.now().timestamp()

    if payload.get('exp') and payload['exp'] < unix_time_now:
        return False
    
    if b64_signature_checker != b64_signature:
        return False
    
    
    return payload

    
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('autho')
        data = verify_and_decode_jwt(token)
        if not data:
            return jsonify({'message': 'token is invalid or expired'}),401
        
        return f(*args, **kwargs)
    
    return decorator

