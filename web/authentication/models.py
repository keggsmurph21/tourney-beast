from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

import us #for state names and abbreviations

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')

        account = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    team_name = models.CharField(max_length=40, blank=True)

    #location
    city = models.CharField(max_length=40, blank=True)
    STATES = us.states.STATES
    STATE_CHOICES = []
    for STATE in STATES:
        STATE_CHOICES.append( (str(STATE.abbr), str(STATE.name)) )
    STATE_CHOICES = tuple(STATE_CHOICES)
    state = models.CharField(max_length=2,
                             choices=STATE_CHOICES,
                             blank=True
    )

    #account type
    PLAYER = 'PL'
    PARENT = 'PA'
    COACH = 'CO'
    ADVERTISER = 'AD'
    ACCT_TYPE_CHOICES = (
        (PLAYER, 'Player'),
        (PARENT, 'Parent'),
        (COACH, 'Coach'),
        (ADVERTISER, 'Advertiser')
    )
    acct_type = models.CharField(max_length=2,
                                 choices=ACCT_TYPE_CHOICES,
                                 blank=True
    )

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def get_location(self):
        return ', '.join([self.city, self.state])
