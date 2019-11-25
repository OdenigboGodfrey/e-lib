from django.shortcuts import render
from  e_lib import app_globals 
from  e_lib.app_globals import AppStrings 
from .classes.item import Item
from client.views import check_params, init_context, json_response, new_message

POST = app_globals.POST
GET = app_globals.GET
POSITIVE = app_globals.POSITIVE
NEUTRAL = app_globals.NEUTRAL
NEGATIVE = app_globals.NEGATIVE

def add(request):
    context = init_context({'id': request.session['staff_user_id']})
    item_types = Item().get_item_types()
    categories = Item().get_categories()

    if item_types['status'] != NEGATIVE:
        context['item_types'] = item_types['item_types']
    
    if categories['status'] != NEGATIVE:
        context['categories'] = categories['categories']
    
    if request.method == POST:
        params_check = check_params(request.POST, { 'published_on': { 'exculded': True }, 'rating': { 'exculded': True }})
        if not params_check['failed']:
            post = request.POST
            staff_id = request.session['staff_id']
            item = Item().add(post['title'], post['author'], post['published_on'], post['category'], post['item_type'], post['price'], post['quantity'], post['rating'], post['summary'], staff_id)
        else:
            context['messages'].extend(params_check['messages'])
    # AppStrings().get_single('no_item_types', 'dict')
    context['app_strings'] = AppStrings().get_multiple(['no_item_types', 'no_categories'])
    return render(request, 'library/add.html', context=context)


def items(request):
    context = init_context()
    items = Item().get()
    if items['status'] != NEGATIVE:
        context['items'] = items['items']
    context['app_strings'] = AppStrings().get_single('failed_to_get_item', 'dict')
    return render(request, 'library/items.html', context=context)

def borrow(request, item_id):
    context = init_context()

