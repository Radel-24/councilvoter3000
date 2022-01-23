from django.db import models

# Create your models here.
class Candidate(models.Model):
	intra = models.CharField(max_length=50)
	name = models.CharField(max_length=200)
	votes = models.PositiveSmallIntegerField(0)

	def __str__(self):
		return self.intra + ' | ' + self.name + ' | ' + str(self.votes)

class Voter(models.Model):
	id_42 = models.CharField(max_length=200)


