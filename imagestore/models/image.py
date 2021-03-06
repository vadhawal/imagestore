#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'

from bases.image import BaseImage
from django.utils.translation import ugettext_lazy as _
from imagestore.utils import load_class, get_model_string
from django.db import models
from mezzanine.blog.models import BlogCategory

class Image(BaseImage):
    class Meta(BaseImage.Meta):
        abstract = False
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        app_label = 'imagestore'

    tagged_categories = models.ManyToManyField(BlogCategory,
                                        verbose_name=_("Tag Categories"),
                                        blank=True, related_name="image")