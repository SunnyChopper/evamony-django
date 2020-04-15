from django.db import models

# Create your models here.
class Family(models.Model):
	address = models.CharField(max_length = 128)
	address_2 = models.CharField(max_length = 32)
	city = models.CharField(max_length = 64)
	zipcode = models.CharField(max_length = 6)
	num_adults = models.IntegerField()
	num_children = models.IntegerField()
	is_active = models.BooleanField(default = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)