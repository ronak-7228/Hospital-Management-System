from django.db import models

# Create your models here.

class Appointments(models.Model):
    doctor = models.OneToOneField('Doctor', models.DO_NOTHING, primary_key=True)
    pid = models.ForeignKey('PatientDetails', models.DO_NOTHING, db_column='pid')
    date = models.DateField()
    prescription = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointments'
        unique_together = (('doctor', 'pid', 'date'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Designation(models.Model):
    designation = models.CharField(db_column='Designation', primary_key=True, max_length=50)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'designation'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class Doctor(models.Model):
    doctor_id = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=50, blank=True, null=True)
    fees = models.IntegerField(blank=True, null=True)
    specialisation = models.ForeignKey('Specialisation', models.DO_NOTHING, db_column='specialisation', blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class PatientDetails(models.Model):
    pid = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_details'


class Specialisation(models.Model):
    specialisation = models.CharField(db_column='Specialisation', primary_key=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specialisation'


class Staff(models.Model):
    sid = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    join_date = models.DateField(blank=True, null=True)
    designation = models.ForeignKey(Designation, models.DO_NOTHING, db_column='designation', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'
