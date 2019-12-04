from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Listing(models.Model):
    listing_id = models.AutoField(db_column='listing_ID', primary_key=True)  # Field name made lowercase.
    rim_model = models.ForeignKey('Rim', models.DO_NOTHING, db_column='rim_model')
    quantity = models.IntegerField()
    price = models.FloatField()
    seller_name = models.CharField(max_length=45)
    seller_phone = models.CharField(max_length=45)
    image = models.CharField(max_length=1000, blank=True, null=True)
    location = models.CharField(max_length=45)
    condition = models.CharField(max_length=45)

    def get_absolute_url(self):
        return reverse("allposts:detail", kwargs={"listing_id": self.pk})
    
    class Meta:
        managed = False
        db_table = 'listing'

    def __str__(self):
        return str(self.listing_id) + ' - ' + str(self.rim_model.rim_model) + ' - ' + self.seller_name
    
    @property
    def get_rim_str(self):
        listing_rim_model = str(self.rim_model.rim_model)
        return listing_rim_model

    def get_rim_key(self):
        return self.rim_model.rim_model


class Manufacturer(models.Model):
    name = models.CharField(primary_key=True, max_length=45)
    website = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturer'
    



class Rim(models.Model):
    rim_model = models.CharField(primary_key=True, max_length=45)
    diameter = models.FloatField()
    width = models.FloatField()
    bolt_pattern = models.CharField(max_length=45)
    offset = models.FloatField()
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_column='manufacturer', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rim'

    def get_manufacturer_key(self):
        return self.manufacturer.name

    @property
    def get_manufacturer_str(self):
        manufacturer_name = str(self.manufacturer.name)
        return manufacturer_name

    def __str__(self):
        return str(self.rim_model)


class Car(models.Model):
    car_id = models.AutoField(db_column='car_id', primary_key=True) 
    year = models.IntegerField()
    make = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    offset = models.FloatField()
    bolt_pattern = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'car'
        unique_together = (('year', 'make', 'model'),)

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

