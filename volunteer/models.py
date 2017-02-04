from django.db import models
from django.db.models.signals import pre_save, post_save

from django.core.urlresolvers import reverse
from django.utils.text import slugify




# Create your models here.


def upload_location(instance, filename):
    return "%s/%s/%s" % ("volunteer", instance.name, filename)

VERIFICATION_CHOICE = (
    (0, "Pending"),
    (1, "Verified"),
)


class Volunteer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15, unique=True)
    website = models.URLField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    content = models.TextField()
    verification_status = models.IntegerField(
        default=0, choices=VERIFICATION_CHOICE)
    image = models.ImageField(upload_to=upload_location, null=True,
                              height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    average_rating = models.IntegerField(default=0)
    blocked = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["-name", ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("volunteer:show_volunteer", kwargs={"slug": self.slug})


def create_slug(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    instance.slug = slug

pre_save.connect(create_slug, sender=Volunteer)

RATING_CHOICE = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)


class Review(models.Model):
    #user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.content


class Report(models.Model):
    #user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    verification_status = models.IntegerField(
        default=0, choices=VERIFICATION_CHOICE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("report_detail", kwargs={"id": self.id})
