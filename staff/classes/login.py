from django.shortcuts import get_object_or_404
from e_lib import app_globals
from staff.models import registration
from client.models import user
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
                user_object = get_object_or_404(user, registration=registration_object.pk)
                data['status'] = POSITIVE
                data['staff'] = registration_object
                data['user'] = user_object
            else:
                raise Exception('wrong_password')
        except Exception as e:
            data['status'] = NEGATIVE
            if "wrong_password" in str(e) :
                data['messages'].append(utils().new_message(NEGATIVE, app_globals.AppStrings().get_single('wrong_password')))
            else:
                data['messages'].append(utils().new_message(NEGATIVE, app_globals.AppStrings().get_single('wrong_email')))
        return data
            
            
