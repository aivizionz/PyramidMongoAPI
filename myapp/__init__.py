from pyramid.config import Configurator
# from pyramid.events import subscriber
from pyramid.events import NewRequest
from pymongo import MongoClient

from myapp.resources import Root


def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings, root_factory=Root)

    config.add_static_view('static', 'myapp:static')

    # Route for Pyramid Home page
    config.add_route('home', '/')
    # Route for login, logout
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    # Route for users data
    config.add_route('users', '/users')
    config.add_route('usersv1', '/v1/users')
    # Route for user search
    config.add_route('usersearch', '/users/{filter}{other:.*}')
    config.add_route('usersearchv1', '/v1/users/{filter}{other:.*}')
    # Route for directory listing
    config.add_route('files', '/files/{path:.*}')
    config.add_route('filesv1', '/v1/files/{path:.*}')
    # Route for service status
    config.add_route('status', '/status/{service}')
    config.add_route('statusv1', '/v1/status/{service}')

    # MongoDB configuration
    def add_mongo_db(event):
        settings = event.request.registry.settings
        # url = settings['mongodb.url']
        # import pdb; pdb.set_trace()
        # db_name = settings['mongodb.db_name']
        conn = settings['mongodb_conn']
        event.request.conn = conn

    db_uri = settings['mongodb.url']
    # MongoDB = pymongo.MongoClient
    # import pdb; pdb.set_trace()
    conn = MongoClient(db_uri)
    config.registry.settings['mongodb_conn'] = conn
    config.add_subscriber(add_mongo_db, NewRequest)
    config.scan('myapp')
    config.include('pyramid_chameleon')
    return config.make_wsgi_app()
