from django.shortcuts import get_object_or_404, get_list_or_404
from e_lib import app_globals
from e_lib.app_globals import AppStrings
from library.models import *
from client.classes.user import User
from .utils import utils


POSITIVE = app_globals.POSITIVE
NEUTRAL = app_globals.NEUTRAL
NEGATIVE = app_globals.NEGATIVE

class Item:
    def add(self, _title, _author, _published_on, _category, _item_type, _price, _quantity, _rating, _summary, uploaded_by, _sub_category=None):
        data = utils().init()
        try:
            item_object = item()

            item_object.item_type = get_object_or_404(item_type, pk=_item_type)
            item_object.title = _title
            item_object.author = _author
            item_object.published_on = _published_on
            item_object.category = get_object_or_404(category, pk=_category)
            item_object.price = _price
            item_object.quantity = _quantity
            item_object.rating = _rating
            item_object.summary = _summary
            item_object.uploaded_by = User().get_user(uploaded_by)['user']

            item_object.save()

            data['status'] = POSITIVE
            data['messages'].append(utils().new_message(POSITIVE, AppStrings().get_single("item_saved"), data=data))
        except Exception as e:
            print(e)
            data['status'] = NEGATIVE
            data['messages'].append(utils().new_message(NEGATIVE, AppStrings().get_single("failed_to_add_item"), data=data))
        return data
    

    def get(self, item_id=None, fetch=app_globals.ALL):
        data = utils().init()
        try:
            if fetch == app_globals.ALL:
                item_object = get_list_or_404(item)
            elif fetch == app_globals.SINGLE:
                if item_id != None:
                    item_object = get_object_or_404(item, id=item_id)
                else:
                    raise Exception('item_id')
            data['items'] = item_object
        except Exception as e:
            data['status'] = NEGATIVE
            if str(e) == 'item_id':
                data['messages'].append(utils().new_message(NEGATIVE, AppStrings().get_single("item_id_needed"), data=data))
            else:
                data['messages'].append(utils().new_message(NEGATIVE, AppStrings().get_single("failed_to_get_item"), data=data))
        return data

    
    def borrow(self, item_id):
        data = utils().init()
        try:
            item = self.get(item_id=item_id, app_globals.SINGLE)
            if item['display_message'] == NEGATIVE:
                # an error occured with getting item
                raise Exception('item_id')
            bor
        except Exception as e:
            data['status'] = NEUTRAL
            if str(e) == 'item_id':
                data['messages'].append(utils().new_message(NEGATIVE, AppStrings().get_single("failed_to_get_item"), data=data))
            else:
                data['messages'].append(utils().new_message(NEGATIVE, AppStrings().get_single("borrow_failed"), data=data))
        
        return data
    
    def get_item_types(self):
        data = utils().init()
        try:
            # 
            item_types = get_list_or_404(item_type)
            # print(item_types)
            data['item_types'] = item_types
        except:
            data['status'] = NEGATIVE
            data['messages'].append(utils().new_message(NEGATIVE, AppStrings().get_single("get_item_types_failed"), data=data))
        return utils().return_data(data)
    

    def get_categories(self):
        data = utils().init()
        try:
            _catgories = get_list_or_404(category)
            print(_catgories)
            data['categories'] = _catgories
        except:
            data['status'] = NEGATIVE
            data['messages'].append(utils().new_message(NEGATIVE, AppStrings().get_single("get_item_types_failed"), data=data)) 
        
        return utils().return_data(data)