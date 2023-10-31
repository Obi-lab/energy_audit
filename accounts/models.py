from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from .managers import UsersManager

# Create your models here.
        
        
class UserAccount(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(("Email"), max_length=254,unique=True)
    is_active=models.BooleanField(("Is Active"), default=True)
    is_staff=models.BooleanField(("Is Staff"), default=False)
    
    
    name=models.CharField(("Name"),blank=True,default='N/A', max_length=100)
    #cover_photo = models.ImageField(upload_to='coverPhotos/',default='N/A', null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS=['email']
    
    objects = UsersManager()
    
    # def get_full_name(self):
    #     return self.name
    
    # def get_short_name(self):
    #     return self.name
    
    def __str__(self):
        return self.email
    

    
    
    
    
