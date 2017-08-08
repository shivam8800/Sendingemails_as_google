from django.db import models
from django.contrib.auth.models import User

class Mail(models.Model):
	user = models.ForeignKey(User)
	Receiver = models.EmailField()
	Subject = models.CharField(max_length=30)
	Message = models.TextField()

	def __str__(self):
		return self.Receiver

# class ReceivingMail(models.Model):
# 	user = models.ForeignKey(Mail)
# 	Sender = models.EmailField()
# 	Subject = models.CharField(max_length=30)
# 	Message = models.TextField()

# 	def __str__(self):
# 		return self.Sender