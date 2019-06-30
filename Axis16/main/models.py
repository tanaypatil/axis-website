from django.db import models
from django.core.validators import RegexValidator


class RobowarsRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, null=False, default=None, unique=True)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    foname = models.CharField(max_length=40, blank=True, null=True, default=None)
    focollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fomail = models.EmailField(blank=True, null=True, default=None)
    focon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    focity = models.CharField(max_length=12, blank=True, null=True, default=None)
    finame = models.CharField(max_length=40, blank=True, null=True, default=None)
    ficollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fimail = models.EmailField(blank=True, null=True, default=None)
    ficon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    ficity = models.CharField(max_length=12, blank=True, null=True, default=None)
    siname = models.CharField(max_length=40, blank=True, null=True, default=None)
    sicollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    simail = models.EmailField(blank=True, null=True, default=None)
    sicon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    sicity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class MechaRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    foname = models.CharField(max_length=40, blank=True, null=True, default=None)
    focollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fomail = models.EmailField(blank=True, null=True, default=None)
    focon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    focity = models.CharField(max_length=12, blank=True, null=True, default=None)
    finame = models.CharField(max_length=40, blank=True, null=True, default=None)
    ficollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fimail = models.EmailField(blank=True, null=True, default=None)
    ficon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    ficity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class AutobotRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    foname = models.CharField(max_length=40, blank=True, null=True, default=None)
    focollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fomail = models.EmailField(blank=True, null=True, default=None)
    focon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    focity = models.CharField(max_length=12, blank=True, null=True, default=None)
    finame = models.CharField(max_length=40, blank=True, null=True, default=None)
    ficollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fimail = models.EmailField(blank=True, null=True, default=None)
    ficon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    ficity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class SkyRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class AquahuntRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    foname = models.CharField(max_length=40, blank=True, null=True, default=None)
    focollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fomail = models.EmailField(blank=True, null=True, default=None)
    focon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    focity = models.CharField(max_length=12, blank=True, null=True, default=None)
    finame = models.CharField(max_length=40, blank=True, null=True, default=None)
    ficollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fimail = models.EmailField(blank=True, null=True, default=None)
    ficon = models.CharField(max_length=12, blank=True, null=True, default=None,
                             validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    ficity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class CrepidoRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    foname = models.CharField(max_length=40, blank=True, null=True, default=None)
    focollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fomail = models.EmailField(blank=True, null=True, default=None)
    focon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    focity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class ParaRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    foname = models.CharField(max_length=40, blank=True, null=True, default=None)
    focollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fomail = models.EmailField(blank=True, null=True, default=None)
    focon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    focity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class TurbofluxRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class AnimazioneRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class CryptocruxRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class PosterolicRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname


class WallstreetRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname


class WhosTheBossRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname


class FreakoRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class CounterStrikeRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, null=False, default=None, unique=True)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    foname = models.CharField(max_length=40, blank=True, null=True, default=None)
    focollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fomail = models.EmailField(blank=True, null=True, default=None)
    focon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    focity = models.CharField(max_length=12, blank=True, null=True, default=None)
    finame = models.CharField(max_length=40, blank=True, null=True, default=None)
    ficollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fimail = models.EmailField(blank=True, null=True, default=None)
    ficon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    ficity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class NFSRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname


class FifaRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname


class TechnoDocxRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, unique=True, null=False, default=None, blank=False, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class MobileRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    foname = models.CharField(max_length=40, blank=True, null=True, default=None)
    focollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fomail = models.EmailField(blank=True, null=True, default=None)
    focon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    focity = models.CharField(max_length=12, blank=True, null=True, default=None)
    finame = models.CharField(max_length=40, blank=True, null=True, default=None)
    ficollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fimail = models.EmailField(blank=True, null=True, default=None)
    ficon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    ficity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class SelfBalRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    foname = models.CharField(max_length=40, blank=True, null=True, default=None)
    focollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fomail = models.EmailField(blank=True, null=True, default=None)
    focon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    focity = models.CharField(max_length=12, blank=True, null=True, default=None)
    finame = models.CharField(max_length=40, blank=True, null=True, default=None)
    ficollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fimail = models.EmailField(blank=True, null=True, default=None)
    ficon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    ficity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class OrnithoRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname


class AndroidRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False,null=False, default=None)
    fcity = models.CharField(max_length=12, blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname


class BakerRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None, unique=True)
    fname = models.CharField(max_length=40, blank=False, unique=True)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    level = models.IntegerField(default=0)
    lastSubmit = models.TimeField(default=None, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-level', 'lastSubmit']

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname


class ManualroboRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, null=False, default=None, unique=True)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    foname = models.CharField(max_length=40, blank=True, null=True, default=None)
    focollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fomail = models.EmailField(blank=True, null=True, default=None)
    focon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    focity = models.CharField(max_length=12, blank=True, null=True, default=None)
    finame = models.CharField(max_length=40, blank=True, null=True, default=None)
    ficollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fimail = models.EmailField(blank=True, null=True, default=None)
    ficon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    ficity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class ElectroRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname


class KartavyaRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class ArchitechRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class DesignoRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, unique=True, null=False, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class PhotoscopeRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname


class BrainRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname


class CollRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, null=False, default=None, unique=True)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    foname = models.CharField(max_length=40, blank=True, null=True, default=None)
    focollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fomail = models.EmailField(blank=True, null=True, default=None)
    focon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    focity = models.CharField(max_length=12, blank=True, null=True, default=None)
    finame = models.CharField(max_length=40, blank=True, null=True, default=None)
    ficollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fimail = models.EmailField(blank=True, null=True, default=None)
    ficon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    ficity = models.CharField(max_length=12, blank=True, null=True, default=None)
    siname = models.CharField(max_length=40, blank=True, null=True, default=None)
    sicollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    simail = models.EmailField(blank=True, null=True, default=None)
    sicon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    sicity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class LaserRegistration(models.Model):

    idnum = models.CharField(max_length=20, default=None)
    team = models.CharField(max_length=20, blank=False, null=False, default=None, unique=True)
    fname = models.CharField(max_length=40, blank=False)
    fcollege = models.CharField(max_length=60, blank=False)
    fmail = models.EmailField(blank=False, unique=True, null=False, default=None)
    fcon = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    fcity = models.CharField(max_length=12, blank=False, null=True)
    sname = models.CharField(max_length=40, blank=True, null=True, default=None)
    scollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    smail = models.EmailField(blank=True, null=True, default=None)
    scon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    scity = models.CharField(max_length=12, blank=True, null=True, default=None)
    tname = models.CharField(max_length=40, blank=True, null=True, default=None)
    tcollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    tmail = models.EmailField(blank=True, null=True, default=None)
    tcon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    tcity = models.CharField(max_length=12, blank=True, null=True, default=None)
    foname = models.CharField(max_length=40, blank=True, null=True, default=None)
    focollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fomail = models.EmailField(blank=True, null=True, default=None)
    focon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    focity = models.CharField(max_length=12, blank=True, null=True, default=None)
    finame = models.CharField(max_length=40, blank=True, null=True, default=None)
    ficollege = models.CharField(max_length=60, blank=True, null=True, default=None)
    fimail = models.EmailField(blank=True, null=True, default=None)
    ficon = models.CharField(max_length=12, blank=True, null=True, default=None, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    ficity = models.CharField(max_length=12, blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team

    def __unicode__(self):
        return self.team


class FeedbackMessage(models.Model):
    name = models.CharField(max_length=40, blank=False)
    mail = models.EmailField()
    con = models.CharField(max_length=12, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    msg = models.TextField(max_length=20000)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
