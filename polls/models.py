from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text



class Club(models.Model):


    nombre= models.CharField(max_length=1000,blank=True, null=True)
    razon_social = models.CharField(max_length=1000,blank=True, null=True)
    ruc = models.CharField(max_length=1000,blank=True, null=True)
    representante = models.CharField(max_length=1000,blank=True, null=True)
    email_repre = models.CharField(max_length=1000,blank=True, null=True)
    telefono = models.CharField(max_length=1000,blank=True, null=True)
    direccion = models.CharField(max_length=1000,blank=True, null=True)
    pagina_web = models.CharField(max_length=1000,blank=True, null=True)
    pagina_red_social = models.CharField(max_length=1000,blank=True, null=True)
    max_usuarios = models.CharField(max_length=1000,blank=True, null=True)

    def __unicode__(self):
        return self.nombre






# from django.db import models
# from django.utils.encoding import python_2_unicode_compatible

# @python_2_unicode_compatible  # only if you need to support Python 2
# class Question(models.Model):
#     # ...
#     def __str__(self):
#         return self.question_text

# @python_2_unicode_compatible  # only if you need to support Python 2
# class Choice(models.Model):
#     # ...
#     def __str__(self):
#         return self.choice_text