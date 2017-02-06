from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone

# Create your models here.
class DonateManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(DonateManager,self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
    # filebase,extension=filename.splot(".")
    # return "%s/%s.%s"%(instance.id,filename,extension)

    return "%s/%s"%(instance.id,filename)



class Donate(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
        slug = models.SlugField(unique=True)
        image = models.ImageField(upload_to=upload_location,
        null=True, blank=True,width_field="width_field",height_field="height_field")
        height_field = models.IntegerField(default=0)
        width_field = models.IntegerField(default=0)
        shirt_qty = models.PositiveIntegerField(default=-1)
        pant_qty = models.PositiveIntegerField(default=0)
        blanket_qty = models.PositiveIntegerField(default=0)
        books_qty = models.PositiveIntegerField(default=0)
        other_qty = models.PositiveIntegerField(default=0)
        furniture_qty = models.PositiveIntegerField(default=0)
        furniture_description=models.TextField(null=True, blank=True)

        objects=DonateManager()

        def __uncode__(self):
            return self.title

        def __str__(self):
            return self.title
        def get_absoulute_url(self):
            return reverse("donate:detail", kwargs={"slug": self.slug})



    # class Meta:
    #     ordering = ["-timestamp","-updated"]
def create_slug(instance,new_slug=None):
    slug = slugify(instance.user)
    if new_slug is not None:
        slug=new_slug
    qs=Donate.objects.filter(slug=slug).order_by("-id")
    exists=qs.exists()
    if exists:
        new_slug="%s-%s"%(slug,qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_donate_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance)

pre_save.connect(pre_save_donate_receiver,sender=Donate)
