# coding: UTF-8
import datetime

from django.db import models
from PIL import Image
from tagging.fields import TagField
from tagging.models import Tag

def make_upload_path(instance, filename):
    """Generates upload path for ImageField"""
    return u"blog/%s%s" % (instance.pub_date.strftime("%Y%m%d%H%M"), filename)

class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = ((LIVE_STATUS, u'Publish'),
                      (DRAFT_STATUS, u'Draft'),
                      (HIDDEN_STATUS, u'Hidden'))

    title = models.CharField(max_length=250,  verbose_name=u'Title')
    body = models.TextField(verbose_name=u'Message')
    image = models.ImageField(upload_to=make_upload_path, blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    views = models.IntegerField(default=0)
    tags = TagField(blank=True)
    meta_keywords = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)

    # some metadata
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)

    class Meta:
        ordering = ['-pub_date']

    def save(self):
        super(Entry, self).save()
        try:
            im = Image.open(self.image)
            im.thumbnail((210,210), Image.ANTIALIAS)
            s= "%s" % self.image.file
            s.replace(".", "copy.")
            im.save(s)
            super(Entry, self).save()
        except:
            pass
    
    def get_tags(self):
        return Tag.objects.get_for_object(self)
    
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
    # link "see on site" will be available in admin site
        return "/weblog/%s/" % (self.id)


