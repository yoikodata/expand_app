from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	"""A Topic the user is learning about"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text


class Entry(models.Model):
	"""Something specific learning about a topic."""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_addded = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Returns a string representation of the model."""
		if len(self.text) < 50:
			return self.text
		else:
			return f"{self.text[:50]}..."