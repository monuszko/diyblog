from django.db.models.signals import post_save 
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import Author


@receiver(post_save, sender=Author)
def add_blogging_permission(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        group = Group.objects.get(name='Bloggers')
        user.groups.add(group)

