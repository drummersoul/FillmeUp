from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.db import models
from django.db.models.signals import pre_save, post_save

from django.utils.text import slugify
from django.core.urlresolvers import reverse

# Create your models here.

def upload_location(instance, filename):
	return "%s/%s/%s" %("user",instance.user.username,filename)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	contact_no = models.CharField(max_length=15, null=True)
	address = models.CharField(max_length=100)
	image = models.ImageField(upload_to=upload_location, null=True, height_field="height_field", width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	bio = models.TextField(null=True)
	birth_date = models.DateField(null=True)
	blocked = models.BooleanField(default=False)
	
	country = models.CharField(max_length=100, null=True)
	slug = models.SlugField(unique=True)


	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse("user:show_profile", kwargs={"slug":self.slug})


def create_slug(sender, instance, *args, **kwargs):
	slug = slugify(instance.user.username,)
	instance.slug = slug

pre_save.connect(create_slug, sender=UserProfile)

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
