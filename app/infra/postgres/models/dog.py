from tortoise import fields
from tortoise.models import Model


class Dog(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20)
    is_adopted = fields.BooleanField(default=False)
    picture = fields.CharField(max_length=100, default="string")
    create_date = fields.DatetimeField(auto_now_add=True)
    user_creator = fields.ForeignKeyField(
        "models.User", on_delete=fields.SET_NULL, null=True, related_name="user_creator"
    )
    user_adopter = fields.ForeignKeyField(
        "models.User", on_delete=fields.SET_NULL, null=True, related_name="user_adopter"
    )

    class Meta:
        table = "dogs"
