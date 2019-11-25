from django.shortcuts import get_object_or_404, get_list_or_404
from e_lib import app_globals
from client.models import registration, user
from .utils import utils
from .user import User


POSITIVE = app_globals.POSITIVE
NEUTRAL = app_globals.NEUTRAL
NEGATIVE = app_globals.NEGATIVE

class Register:

    def handler(self, name, email, dob, gender, password):
        data = utils().init()
        try:
            email_check = registration.objects.filter(email=email)
            if len(email_check) > 0:
                # email is taken
                raise Exception('email')

            
            register_object = registration()
            register_object.first_name=name['first_name']
            register_object.last_name=name['last_name']
            register_object.middle_name= name['middle_name']
            register_object.dob=dob
            register_object.email=email
            register_object.gender=gender
            register_object.password=utils().hash_password(password)

            register_object.save()

            register_object = get_object_or_404(registration, email=email)

            res = User().new_user(app_globals.USER, register_object.pk)
            
            register_object.user_recorded = res['status']
            register_object.save()

            data['status'] = POSITIVE
            data['messages'].append(utils().new_message(POSITIVE, app_globals.AppStrings().get_single("registration_ok"), data=data))
        except Exception as e:
            print (e)
            if 'email' in str(e):
                data['messages'].append(utils().new_message(NEGATIVE, app_globals.AppStrings().get_single("email_taken"), data=data))
            else:
                data['messages'].append(utils().new_message(NEGATIVE, app_globals.AppStrings().get_single("error_occured"), data=data))
        
        return utils().return_data(data)