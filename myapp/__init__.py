from pyramid.config import Configurator
# from pyramid.events import subscriber
from pyramid.events import NewRequest
import pymongo

from myapp.resources import Root


def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings, root_factory=Root)
    config.include('pyramid_chameleon')
    config.add_view('myapp.views.my_view',
                    context='myapp:resources.Root',
                    renderer='myapp:templates/mytemplate.pt')
    config.add_static_view('static', 'myapp:static')

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

    # MongoDB = pymongo.MongoClient()
    # if 'pyramid_debugtoolbar' in set(settings.values()):
    #     class MongoDB(pymongo.Connection):
    #         def __html__(self):
    #             return 'MongoDB: <b>{}></b>'.format(self)
    db_uri = settings['mongodb.url']
    conn = pymongo.MongoClient(db_uri)
    config.registry.settings['mongodb_conn'] = conn

    # MongoDB configuration
    def add_mongo_db(event):
        settings = event.request.registry.settings
        # url = settings['mongodb.url']
        db_name = settings['mongodb.db_name']
        db = settings['mongodb_conn'][db_name]
        event.request.db = db

    config.add_subscriber(add_mongo_db, NewRequest)
    config.scan('myapp')
    return config.make_wsgi_app()
