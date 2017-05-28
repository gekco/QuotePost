from django.db import models

# Create your models here.
class Quotes(models.Model):
	class Meta:
		unique_together = (('userName', 'quote'),)
	userName = models.CharField(max_length=100 )
	quote = models.TextField()
	isAlreadyPosted = models.BooleanField()
	def __str__(self):
		return self.quote