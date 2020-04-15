from django.db import models

# Create your models here.
class ServiceInterest(models.Model):
	is_adult = models.BooleanField()
	adult_id = models.ForeignKey('adults.Adult', blank = True, null = True, on_delete = models.CASCADE)
	child_id = models.ForeignKey('children.Child', blank = True, null = True, on_delete = models.CASCADE)
	title = models.CharField(max_length = 64)
	is_active = models.BooleanField(default = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)