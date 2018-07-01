from mongoengine import *
from CloudCove.settings import DBNAME

connect(DBNAME)

class UserDetails(Document):
    username = StringField(max_length=120, required=True)
    password = StringField(max_length=50, required=True)
    address = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)
    tags = ListField(StringField(max_length=30))

