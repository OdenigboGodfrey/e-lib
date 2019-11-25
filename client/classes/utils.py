from e_lib import app_globals 
import hashlib

POSITIVE = app_globals.POSITIVE
NEUTRAL = app_globals.NEUTRAL
NEGATIVE = app_globals.NEGATIVE
PASSWORD_SALT = app_globals.PASSWORD_SALT

class utils:
    def init(self):
        return { 'status': NEUTRAL, 'messages': [], 'display_message': NEUTRAL }

    def new_message(self, status, message, data=None):
        if data is not None and data['display_message'] is NEUTRAL: 
            # if message is not a nuetral message, update displaymessages to make it shown to client
            data['display_message'] = status
        return { 'status': status, 'message': message }

    def return_data(self, old_data, status=None, message=None, extra_data=None):
        if status is not None:
            old_data['status'] = status
        if message is not None:
            old_data['messages'].append(self.new_message(status, message))
        if extra_data is not None:
            old_data.update(extra_data)
        
        return old_data

    def hash_password(self, password):
        return hashlib.md5(
            PASSWORD_SALT.encode() + (hashlib.sha1(password.encode()).hexdigest()).encode()).hexdigest()