from e_lib import app_globals
from e_lib.app_globals import AppStrings
from client.models import user
from django.shortcuts import get_object_or_404, get_list_or_404
from .utils import utils

POSITIVE = app_globals.POSITIVE
NEUTRAL = app_globals.NEUTRAL
NEGATIVE = app_globals.NEGATIVE

class User:
    utils_object = utils()

    def new_user(self, user_type, registration_id):
        data = self.utils_object.init()
        try:
            user_object = user()
            user_object.user_type = user_type
            user_object.registration = registration_id

            user_object.save()
        except Exception as e:
            print (e)
            data['status'] = NEGATIVE
            data['messages'].append(self.utils_object.new_message(NEGATIVE, AppStrings().get_single("new_user_failed")))
        
        return self.utils_object.return_data(data)
    
    def get_user(self, registration_id):
        data = self.utils_object.init()
        try:
            user_object = get_object_or_404(user, registration=registration_id)
            print(user_object)
            data['user'] = user_object
        except Exception as e:
            print(e)
            data['status'] = NEGATIVE
            data['messages'].append(self.utils_object.new_message(NEGATIVE, AppStrings().get_single("user_get_failed")))
        
        return self.utils_object.return_data(data)