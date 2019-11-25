from django.shortcuts import render
from  e_lib import app_globals 
from .classes.register import Register
from .classes.login import Login

POST = app_globals.POST
GET = app_globals.GET
POSITIVE = app_globals.POSITIVE
NEUTRAL = app_globals.NEUTRAL
NEGATIVE = app_globals.NEGATIVE

def init_context(context=None, extra_info=None):
    if context is None:
        context = { 'POSITIVE': 1, 'NEUTRAL': 0, 'NEGATIVE': 1, 'messages': [], 'display_message': NEUTRAL }
    if extra_info is not None:
        context.update(extra_info)
    return context

def new_message(status, message, context=None):
    if context is None:
        return {'status': status, 'message': message}
    if 'messages' in context:
        context['messages'].append({'status': status, 'message': message})
    else:
        context['messages'] = [{'status': status, 'message': message}]

def merge_messages(context, result):
    for message in result['messages']:
        if message['status'] != NEUTRAL:
            context['messages'].append(message)
            if context['display_message'] == NEUTRAL:
                context['display_message'] = message['status']

def json_response(context):
    return 'n/a'

def check_params(post, look_out=None):
    messages = []
    for key in post:
        value = post[key]
        if look_out is not None and key in look_out:
            # make extra checks
            if 'excluded' in post[key] and post[key].excluded:
                continue
            if 'expected_type' in look_out[key]:
                try:
                    # cast value to passed type
                    look_out[key]['expected_type'](value)
                except Exception as e:
                    messages.append(new_message(status=NEGATIVE, message=key.replace('_',' ').upper() + " expects " + look_out[key]['string_representation']))
        else:
            if value is None or not value:
                messages.append(new_message(status=NEGATIVE, message=key.replace('_','').upper() + " is required."))
    return { 'messages': messages, 'failed': len(messages) > 0 }

def register(request):
    context = init_context()
    if request.method == POST:
        # , 'email': {'expected_type': int, 'string_representation': 'an email address'}
        params_check = check_params(request.POST, { 'middle_name': { 'exculded': True }})
        if not params_check['failed']:
            if request.POST['password'] == request.POST['confirm_password']:
                result = Register().handler(name={ 'first_name': request.POST['first_name'], 'last_name': request.POST['last_name'], 'middle_name': request.POST['middle_name'] }, email=request.POST['email'], dob=request.POST['dob'], gender=request.POST['gender'], password=request.POST['password'])
                

                if result['display_message'] != NEUTRAL:
                    merge_messages(context, result)
            else:
                context['messages'].extend(new_message(NEGATIVE, app_globals.AppStrings().get_single("password_not_same"), context=context))
        else:
            context['messages'].extend(params_check['messages'])
    if 'json' in request.GET:
        return json_response(context)
    return render(request, 'staff/register.html', context=context)

def login(request):
    context = init_context()
    if request.method == POST:
        params_check = check_params(request.POST)
        if not params_check['failed']:
            result = Login().handler(request.POST['email'], request.POST['password'])
            
            if result['status'] == POSITIVE:
                request.session['staff_id'] = result['staff'].pk
                request.session['staff_name'] = { 'first_name': result['staff'].first_name, 'last_name': result['staff'].last_name, 'middle_name': result['staff'].middle_name }
                request.session['staff_email'] = result['staff'].email
                request.session['staff_user_id'] = result['user'].pk

                if 'json' in request.GET:
                    return json_response(result)
                print('logged in')
            elif result['status'] == NEGATIVE:
                merge_messages(context, result)
                
        else:
            context['messages'].extend(params_check['messages'])
    
    if 'json' in request.GET:
        return json_response(result)
    return render(request, 'staff/login.html', context=context)