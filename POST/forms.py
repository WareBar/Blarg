from django import forms
from . import models



class createPost(forms.ModelForm):
	class Meta:
		model = models.Post
		fields = ['title','content','banner',]