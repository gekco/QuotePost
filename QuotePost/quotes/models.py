from django.db import models

# Create your models here.
#Table quotes contain following fields
#1. userName -> username of user
#2. quote ->quote saved/posted by user
#3. isAlreadyPosted -> true if posted false otherwise
class Quotes(models.Model):
	class Meta:
		unique_together = (('userName', 'quote'),)
	userName = models.CharField(max_length=100 )
	quote = models.TextField()
	isAlreadyPosted = models.BooleanField()
	def __str__(self):
		return self.quote