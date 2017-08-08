from django.db import models
from django.contrib.auth.models import User

class Mail(models.Model):
	user = models.ForeignKey(User)
	Receiver = models.EmailField()
	Subject = models.CharField(max_length=30)
	Message = models.TextField()
	is_deleted_receiver = models.BooleanField(default=False)
	is_deleted_sender =  models.BooleanField(default=True)


	def __str__(self):
		return self.Receiver