from ..models.data_transactions.CRUD import \
create_data_transactions, delete_user

def create_data(data):
    return create_data_transactions(data)
def delete_transactions(id):
    return delete_user(id)