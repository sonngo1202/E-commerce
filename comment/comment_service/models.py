from django.db import models

class Comment(models.Model):
    user_id = models.CharField(max_length=7)
    product_id = models.CharField(max_length=7)
    comment = models.CharField(max_length=250)
    rate = models.IntegerField()
    type = models.CharField(max_length=10, null=True)
    date_added = models.DateField(auto_now_add=True)