from django.db import models

# Create your models here.
class Child(models.Model):
	family = models.ForeignKey('family.Family', on_delete = models.CASCADE)
	first_name = models.CharField(max_length = 64)
	last_name = models.CharField(max_length = 64)
	picture_url = models.CharField(max_length = 256)
	family_role = models.CharField(max_length = 64)
	sex = models.IntegerField()
	phone_number = models.CharField(max_length = 16)
	dob_month = models.CharField(max_length = 16)
	dob_day = models.IntegerField()
	dob_year = models.IntegerField()
	email = models.CharField(max_length = 64)
	grade_level = models.CharField(max_length = 64)
	is_active = models.BooleanField(default = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)