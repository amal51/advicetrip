import cgi
import wsgiref.handlers
import os

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from com.ujinsung.advicetrips.question import QuestionForm

class MainPage(webapp.RequestHandler):
  def get(self):
#    choice = QuestionForm()
    choice = QuestionForm()
    q = "test"
    
    if users.get_current_user():
      login_url = users.create_logout_url(self.request.uri)
      login_url_linktext = 'Logout'
    else:
      login_url = users.create_login_url(self.request.uri)
      login_url_linktext = 'Login'
    template_values = {
      'question': q,
      'form': choice,
      'login_url': login_url,
      'login_url_linktext': login_url_linktext,
      }
    
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

class SubmitForm(webapp.RequestHandler):
  def post(self):
    self.redirect('/')
        
def main():
    application = webapp.WSGIApplication (
                                          [('/', MainPage),
                                           ('/submit', SubmitForm)],
                                          debug=True)
    wsgiref.handlers.CGIHandler().run(application)
    
if __name__ == "__main__":
    main()