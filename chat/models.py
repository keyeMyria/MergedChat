from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


class Room(models.Model):
    """
    A room for people to chat in.
    """

    # Room title
    title = models.CharField(max_length=255)

    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def group_name(self):
        """
        Returns the Channels Group name that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return "room-%s" % self.id

# class SiteUser(models.Model):
        
#     user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)

#     ## additional fields
#     phone = models.IntegerField(blank=True, default=0)    
#     activation_key = models.CharField(max_length=255, default=1)
#     ZIP = models.CharField(max_length=5, default=1)
#     email_validated = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username        

class ChatMessage(models.Model):
    """
    Model to represent user submitted changed to a resource guide
    """

    #Fields
    created     = models.DateTimeField(editable=False)
    updated    = models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=3000)
    message_html = models.TextField()
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String to represent the message
        """

        return self.message    

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ChatMessage, self).save(*args, **kwargs)        
        


  
