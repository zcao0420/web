# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Draws(models.Model):
    drawid = models.CharField(db_column='DrawID', max_length=10, primary_key=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=20)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score')  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.

    class Meta:
        """
        Deliberately made the managed = False because this django project
        is not supposed to modify MySQL database from AWS.
        The only allowed action is read.
        """
        managed = False
        db_table = 'Draws'


class Pool(models.Model):
    date = models.CharField(db_column='Date', max_length=20, primary_key=True)  # Field name made lowercase.
    lv1 = models.IntegerField(db_column='Lv1')  # Field name made lowercase.
    lv2 = models.IntegerField(db_column='Lv2')  # Field name made lowercase.
    lv3 = models.IntegerField(db_column='Lv3')  # Field name made lowercase.
    lv4 = models.IntegerField(db_column='Lv4')  # Field name made lowercase.
    lv5 = models.IntegerField(db_column='Lv5')  # Field name made lowercase.
    lv6 = models.IntegerField(db_column='Lv6')  # Field name made lowercase.
    lv7 = models.IntegerField(db_column='Lv7')  # Field name made lowercase.
    lv8 = models.IntegerField(db_column='Lv8')  # Field name made lowercase.
    lv9 = models.IntegerField(db_column='Lv9')  # Field name made lowercase.
    lv10 = models.IntegerField(db_column='Lv10')  # Field name made lowercase.
    lv11 = models.IntegerField(db_column='Lv11')  # Field name made lowercase.
    lv12 = models.IntegerField(db_column='Lv12')  # Field name made lowercase.
    lv13 = models.IntegerField(db_column='Lv13')  # Field name made lowercase.
    lv14 = models.IntegerField(db_column='Lv14')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pool'
