from google.appengine.ext import ndb

import datetime
from src import common
from src.handlers.base import BaseHandler
from src.jinja import JINJA_ENVIRONMENT
from src.models.championship import Championship
from src.models.region import Region
from src.models.state import State


class RegionalsHandler(BaseHandler):
  def get(self):
    # The year we want to display championships for.  We should update this
    # once we're ready to start announcing the next year's championships.
    year = datetime.datetime.now().year

    championships = Championship.query(ndb.AND(Championship.year == year,
                                               Championship.region != None)).fetch()
    competitions = ndb.get_multi([c.competition for c in championships])

    states = State.query().fetch()
    regions = Region.query().order(Region.name).fetch()

    championships.sort(key=lambda championship: championship.competition.get().start_date)
    championship_regions = [championship.region for championship in championships]
    regions_missing_championships = [
        region for region in regions if region.key not in championship_regions]

    #If not one of the regionals has happened yet, then show the previous year's champions
    champion_year = year-1 if len(regions_missing_championships) == 7 else year 

    template = JINJA_ENVIRONMENT.get_template('regional.html')
    self.response.write(template.render({
        'c': common.Common(self),
        'year': year,
        'champion_year':champion_year,
        'championships': championships,
        'regions_missing_championships': regions_missing_championships,
    }))
