from django.shortcuts import render, redirect
from  e_lib import app_globals 
from  e_lib.app_globals import AppStrings 
from .classes.item import Item
from client.views import check_params, init_context, json_response, new_message
from datetime import datetime

POST = app_globals.POST
GET = app_globals.GET
POSITIVE = app_globals.POSITIVE
NEUTRAL = app_globals.NEUTRAL
NEGATIVE = app_globals.NEGATIVE

def prepare_borrowed(borrowed):
    now = datetime.now().date()
    tbr = []
    for child in borrowed:
        mini = {'item': child.item, 'borrowed_on': child.borrowed_on}
        then = child.borrowed_on.date()
        tdelta = now - then
        mini['days_left'] = child.max_duration - tdelta.days
        tbr.append(mini)

    return tbr

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
    items = Item().get(fetch=app_globals.ALL)
    if items['status'] != NEGATIVE:
        context['items'] = items['items']
    context['app_strings'] = AppStrings().get_single('failed_to_get_item', 'dict')
    return render(request, 'library/items.html', context=context)

def borrow(request, item_id):
    context = init_context()
    registration_id = 0
    if 'staff_id' in request.session:
        registration_id = request.session['staff_id']
    elif 'client_id' in request.session:
        registration_id = request.session['client_id']
    borrowed = Item().borrow(item_id, registration_id)
    print(borrowed)

    if 'json' in request.GET:
        return json_response(context)
    else:
        return redirect('library:library-get-items')


def borrowed(request, user_id):
    context = init_context()
    borrowed = Item().get_borrowed_items(user_id)
    if borrowed['status'] != NEGATIVE:
        context['borrowed'] = prepare_borrowed(borrowed['borrowed'])
    
    context['app_strings'] = AppStrings().get_single('failed_to_get_borrowed_items', 'dict')
    if 'json' in request.GET:
        return json_response(context)
    return render(request, 'library/borrowed.html', context=context)
