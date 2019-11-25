from django.shortcuts import get_object_or_404
from e_lib import app_globals
from client.models import registration
from .utils import utils

POSITIVE = app_globals.POSITIVE
NEUTRAL = app_globals.NEUTRAL
NEGATIVE = app_globals.NEGATIVE



class Login:
    def handler(self, email, password):
        data = utils().init()
        try:
            registration_object = get_object_or_404(registration, email=email)
            if utils().hash_password(password) == registration_object.password:
                data['status'] = POSITIVE
                data['client'] = registration_object
            else:
                raise Exception('wrong_password')
        except Exception as e:
            data['status'] = NEGATIVE
            if "wrong_password" in str(e) :
                data['messages'].append(utils().new_message(NEGATIVE, app_globals.AppStrings().get_single('wrong_password')))
            else:
                data['messages'].append(utils().new_message(NEGATIVE, app_globals.AppStrings().get_single('wrong_email')))
        return data
            
            
