from contextvars import ContextVar


Transaction_Id = ContextVar('transaction_id', default='')
In_Transaction_Id = ContextVar('transaction_id', default='')
Key_Fields = ContextVar('key_fields', default='')

def set_log_context(transaction_id=None, in_transaction_id=None, **kwargs):
    if transaction_id: Transaction_Id.set(transaction_id) 
    if in_transaction_id: In_Transaction_Id.set(in_transaction_id)
    kf = '' 
    for key, value in kwargs.items():
        kf= f'{kf}{key}={str(value)} | '
    Key_Fields.set(kf)
    
def get_log_context():
    return { 'transaction_id': Transaction_Id.get(), 'in_transaction_id': In_Transaction_Id.get(), 'key_fields': Key_Fields.get()}