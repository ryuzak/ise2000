# -*- encoding: utf-8 -*-
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string

from ferreteria_back.utils import sendmail
from ferreteria_back.tokens import account_activation_token
from ferreteria_back import settings

from decouple import config
# Create your models here.

def user_filename(self, filename):
    url = "accounts_picture/%s/%s" % (self.id, filename)
    return url

# Create your models here.
#-- Create_user extendido de AbstractBaseUser
class UserManager(BaseUserManager):

    def create_user(self, email, password=None):

        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_staff=False,
            is_superuser=False
        )
 #       print(password)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email = self.normalize_email(email),
            is_active=True,
            is_superuser=True,
            is_staff=True,
            #is_superadmin=True
        )
        user.set_password(password)
        user.save()
        return user
 

#-- Clase abstracta extendida del modelo User
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    #-- Atributos adicionales
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=user_filename, blank=True)
    
    USERNAME_FIELD = 'email'
    
    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'users'
        ordering = ['id',]

    @staticmethod
    def activation_email(domain,user,password):
       
        #-- Send email
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)
            
        subject = 'ISE 2000 :: Registro de cuenta'
        message = render_to_string('accounts/accounts_email.html', {
                                    'email': user.email,
                                    'password': password,
                                    'domain': domain,
                                    'uid': uid,
                                    'token': token,
                                    })

        expires_key = datetime.today() + timedelta(2)
        #-- Save activation token
        user_activation = UserRequest.objects.create(user=user, uid=uid, token=token, expires_key=expires_key)

        sendmail(subject, message, settings.DEFAULT_FROM_EMAIL, user.email)

        return True

    @staticmethod
    def activation_url(uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            user_activation = UserRequest.objects.filter(token=token).first()
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token) and user_activation.activation_status == 0:
            user.is_active = True
            user.save()
            user_activation.activation_status = 1
            user_activation.save()

            return user
        else:
            return False


#-- Clase extendia del User para control de las llaves de activacion (Activacion / Solicitud de Contraseña / Invitacion)
class UserRequest(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #-- Keys para la validacion por email cuando de crea el usuario
    activation_key = models.CharField(max_length=40, blank=True)
    expires_key = models.DateTimeField(default=datetime.now)
    uid = models.CharField(max_length=20, default='')
    token = models.CharField(max_length=60, default='')
#    activation_type = models.CharField(max_length=2, choices=ut.ACTIVATION_CHOICES, default='1')
    activation_status = models.BooleanField(default=False)
    activation_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users_request'