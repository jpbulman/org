from google.appengine.ext import ndb

class AppSettings(ndb.Model):
  session_secret_key = ndb.StringProperty()
  wca_oauth_client_id = ndb.StringProperty()
  wca_oauth_client_secret = ndb.StringProperty()  
  google_maps_api_key = ndb.StringProperty()
  recaptcha_site_key = ndb.StringProperty()
  recaptcha_secret_key = ndb.StringProperty()
  contact_email = ndb.StringProperty()

  @staticmethod
  def Get():
    return AppSettings.get_by_id('1') or AppSettings(id='1')
