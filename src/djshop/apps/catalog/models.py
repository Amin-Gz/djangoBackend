from treebeard.mp_tree import MP_Node
from django.db import models

from djshop.apps.catalog.managers import CategoryQuerySets


# Create your models here.
class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=2048,null=True , blank=True)
    is_public = models.BooleanField(default=True)
    slug = models.SlugField()

    objects = CategoryQuerySets.as_manager()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"