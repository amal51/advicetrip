from google.appengine.ext.db import djangoforms
from google.appengine.ext import db

class Question ( db.Model ):
  PLACE_TYPES = (
    (1, 'Bar'),
    (2, 'Restaurant'),
    (3, 'Movie Theater'),
    (4, 'Secret Hideout'),
  )

  answer = db.IntegerProperty(choices=PLACE_TYPES)
  
class QuestionForm ( djangoforms.ModelForm ):
  class Meta:
    model = Question