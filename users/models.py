from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Create your models here.


class CustomUser(AbstractUser):
    
    age = models.PositiveIntegerField(_('your age'), null = True, blank = True)
    date_joined = models.DateTimeField(default=timezone.now)
    email = models.EmailField(_('email address'), unique = True)
    domens = ['online', 'csa', 'telecom']

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'age']

    #checking domain name
    # def clean(self):
    #     if '@' in self.email:
    #         email_domain = self.email.split('@')[-1]
    #         i = 0
    #         for dom in self.domens:
    #             if dom in email_domain:
    #                 i+=1
    #         if i == 0:
    #             raise ValidationError({
    #                 'email': ValidationError(_('Only Kazaktelekom users can be access to the website.'))
    #             })
    #     else:
    #         raise ValidationError({
    #             'email': ValidationError(_('Try to type correct email.'))
    #         })
