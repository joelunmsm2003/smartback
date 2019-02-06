from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

from django.db import models

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


class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    SUPERVISOR = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (SUPERVISOR, 'Supervisor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, blank=True, null=True)
    #birthdate = models.DateField(null=True, blank=True)
    #role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)









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