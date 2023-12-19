from django.db import models

# Create your models here.


'''
class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
'''

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	qrcode_id = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	br =  models.CharField(max_length=50)
	reworked =  models.CharField(max_length=100)
	cont = models.CharField(max_length=15)
	verification =  models.CharField(max_length=100)


	def __str__(self):
		return(f"{self.name} {self.qrcode_id}")
