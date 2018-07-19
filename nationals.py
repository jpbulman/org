import webapp2

from src import config
from src import handlers
from src.handlers.basic import BasicHandler
from src.handlers.contact import ContactHandler
from src.models.user import Roles
from src.handlers.nationals.eighteen.events import Events2018Handler
from src.handlers.nationals.eighteen.groups import Groups2018Handler
from src.handlers.nationals.eighteen.schedule import Schedule2018Handler

uri_base = '/nationals/2018'
template_base = 'nationals/2018'

app = webapp2.WSGIApplication([
  webapp2.Route('/nationals', webapp2.RedirectHandler, defaults={'_uri': '/nationals/2018'}),
  webapp2.Route('/nationals/2018',
                handler=BasicHandler('/nationals/2018/index.html',
                                     include_wca_disclaimer=True)),
  webapp2.Route('/nationals/2018/events', handler=Events2018Handler,
                name='events'),
  webapp2.Route('/nationals/2018/schedule', handler=Schedule2018Handler),
  webapp2.Route('/nationals/2018/travel',
                handler=BasicHandler('/nationals/2018/travel.html')),
  webapp2.Route('/nationals/2018/unofficial',
                handler=BasicHandler('/nationals/2018/unofficial.html')),
  webapp2.Route('/nationals/2018/contact',
                handler=ContactHandler('nats-organizers@cubingusa.org',
                                       '/nationals/2018/contact.html',
                                       'Nationals 2018')),
  webapp2.Route('/nationals/2018/groups', handler=Groups2018Handler,
                name='groups_2018'),
  webapp2.Route('/nationals/2018/groups/<person_id:\d\d\d\d\w\w\w\w\d\d>',
                handler=Groups2018Handler, name='groups_2018_person'),
  webapp2.Route('/nationals/2018/groups/<event_id:.*>/<round_num:\d>/<stage:.>/<group:\d*>',
                handler=Groups2018Handler, name='groups_2018_group'),
], config=config.GetAppConfig())
