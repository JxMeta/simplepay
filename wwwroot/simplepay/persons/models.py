# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

class Tag(models.Model):
    name = models.CharField('Tag', max_length=256)

    nav_display = models.BooleanField('Navigate', default=False)
    home_display = models.BooleanField('Home', default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tag', args=(self.name,))

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'
		ordering = ['name']

class Person(models.Model):
    name = models.CharField('Name', max_length=256)

    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))
    sex = models.CharField('Gender', max_length=1, choices=SEX_CHOICES, default=MALE)

    age = models.IntegerField('Age', default=0)

    YES = 'Y'
    NO = 'N'
    ACTIVE_CHOICES = ((YES, 'Yes'),	(NO, 'No'))
    active = models.CharField('Active', max_length=1, choices=ACTIVE_CHOICES, default=YES)
    
    tags = models.ManyToManyField(Tag, verbose_name='Tag')

    pub_date = models.DateTimeField('Publish Date', auto_now_add=True)
    update_date = models.DateTimeField('Update Date', auto_now=True, null=True)

    def __str__(self):
		return self.name

    def get_absolute_url(self):
        return reverse('person', args=(self.name,))

    class Meta:
		verbose_name = 'Person'
		verbose_name_plural = 'Persons'
