from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=25)
    last_name = fields.CharField(max_length=25)
    email = fields.CharField(unique=True, max_length=50)
    password = fields.CharField(max_length=100)

    class Meta:
        table = "users"
