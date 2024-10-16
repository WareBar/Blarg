from django.db import models
from django.template.defaultfilters import slugify #slugify a string for navigating
from django.contrib.auth.models import User #importing the User Model
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	banner = models.ImageField(default="perl.png", blank=True)

	author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	slug = models.SlugField(blank=True)
	posted_at = models.DateTimeField(auto_now_add=True)


	def save(self, *args, **kwargs):
		if self.slug:
			pass
		else:
			self.slug = slugify(self.title.lower())

		super().save(*args, **kwargs)

	def __str__(self) -> str:
		return self.title