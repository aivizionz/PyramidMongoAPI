import os
import subprocess
# import json
# import sys
from time import strftime
# from pyramid.response import Response
from pyramid.view import (view_config,
                          forbidden_view_config,)
from pyramid.security import (remember,
                              forget,)
from pyramid.httpexceptions import HTTPFound

from .models import (verify_login,
                     users_all,
                     users_filterby,
                     users_flt_groupby)
from .jsondata import USERS
# from .security import LUSERS


def my_view(request):
    return {'project': 'myapp'}


@view_config(route_name='users', renderer='json', request_method='GET')
@view_config(route_name='usersv1', renderer='json', request_method='GET')
def get_users(request):
    """ This method return all user data """
    # return USERS
    return users_all()


@view_config(route_name='usersearch', renderer='json', request_method='GET')
@view_config(route_name='usersearchv1', renderer='json', request_method='GET')
def get_user_search(request):
    """ This method return the users based on the search criteria"""
    # import pdb; pdb.set_trace()
    flt = request.matchdict['filter']
    key, value = flt.split('=')
    fkey = str(key.lower())
    fvalue = str(value.lower())
    grpby = request.matchdict['other']
    grpby = grpby.split('/')
    if len(grpby) >= 2:
        grpby = str(grpby[1])
        grpby = grpby.lower()
        # return user_filter(fkey, fvalue)
        return users_flt_groupby(fkey, fvalue, grpby)
    else:
        return users_filterby(fkey, fvalue)


def user_filter(key, value):
    """ This method return the users based on the filters"""
    users = []
    for i in USERS:
        if key == 'profession' or key == 'genre':
            for j in i[key]:
                if value == j.lower():
                    users.append(i.copy())
        else:
            if i[key].lower() == value:
                users.append(i.copy())
    return users


@view_config(route_name='files', renderer='json', request_method='GET')
@view_config(route_name='filesv1', renderer='json', request_method='GET')
def get_listdir(request):
    """ This method returns the list of files for a given directory """
    # import pdb; pdb.set_trace()
    loc = '../'
    path = str(request.matchdict['path'])
    path = loc + path
    try:
        return [os.path.join(path, files) for files in os.listdir(path)]
    except Exception, e:
        raise e


@view_config(route_name='status', renderer='json', request_method='GET')
@view_config(route_name='statusv1', renderer='json', request_method='GET')
def get_service_status(request):
    """ This method returns the status of service """
    svc = str(request.matchdict['service'])
    try:
        svc_stat = subprocess.Popen(['ps', '-C', str(svc)],
                                    stdout=subprocess.PIPE).communicate()[0].split(b'\n')
    except Exception, e:
        raise e
    # import pdb; pdb.set_trace()
    if len(svc_stat) >= 3:
        svc_stat = svc_stat[1].split(" ")
        pid, svc = svc_stat[1], svc_stat[-1]
        cur_time = strftime("%a, %d %b %Y %X")
        return "Current Time : {0}".format(cur_time), "Service  {0} running: Processid {1}".format(svc, pid)
    else:
        return "Service  {0} not running ".format(svc)


"""
@view_config(route_name='usersearch', renderer='json', request_method='GET')
@view_config(route_name='usersearchv1', renderer='json', request_method='GET')
def get_user_search(request):
    # import pdb; pdb.set_trace()
    key = request.matchdict['filter']
    others = request.matchdict['other']
    return USERS[key], key, others

"""


@view_config(route_name='login', renderer='templates/login.pt')
@forbidden_view_config(renderer='templates/login.pt')
def login(request):
    """ This method handles the login page and authentication """
    login_url = request.route_url('login')
    # import pdb; pdb.set_trace()
    referrer = request.url
    if referrer == login_url:
        referrer = '/'  # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    message = ''
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        # import pdb;pdb.set_trace()
        login = request.params['login']
        password = request.params['password']
        if verify_login(login) == password:
            headers = remember(request, login)
            return HTTPFound(location=came_from,
                             headers=headers)
        message = 'Failed login'

    return dict(
        message=message,
        url=request.application_url + '/login',
        came_from=came_from,
        login=login,
        password=password,)


@view_config(route_name='logout')
def logout(request):
    """ This method redirects to login page """
    headers = forget(request)
    return HTTPFound(location=request.route_url('login'),
                     headers=headers)
