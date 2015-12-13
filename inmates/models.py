from django.db import models
import datetime
import pandas as pd

NULLS = dict(blank=True, null=True)


class PrisonFacility(models.Model):
    class Meta:
        verbose_name_plural = "Prision Facilities"

    name = models.CharField(max_length=100, **NULLS)
    phone_number = models.CharField(max_length=100, **NULLS)

    def __unicode__(self):
        return str(self.name)


class CellBlock(models.Model):
    facility = models.ForeignKey(PrisonFacility, **NULLS)
    block_number = models.IntegerField(**NULLS)

    def __unicode__(self):
        return "<CellBlock {}: {}>".format(self.block_number,
                                           self.facility.name)


class PrisonCell(models.Model):
    cell_block = models.ForeignKey(CellBlock, **NULLS)
    cell_number = models.IntegerField(**NULLS)


    def __unicode__(self):
        return "<Cell: {}, block: {}, facility: {}>".format(
            self.cell_number,
            self.cell_block.block_number,
            self.cell_block.facility
        )


class Gang(models.Model):
    name = models.CharField(max_length=100, **NULLS)
    rivals = models.ForeignKey('self', **NULLS)

    def __unicode__(self):
        return "{}".format(self.name)


class Officer(models.Model):
    first_name = models.CharField(max_length=100, **NULLS)
    last_name = models.CharField(max_length=100, **NULLS)
    badge_number = models.IntegerField(**NULLS)

    def __unicode__(self):
        return "Officer {} {}".format(self.first_name, self.last_name)






class Inmate(models.Model):
    # Name & Basic info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, **NULLS)
    social_secutity_number = models.IntegerField(**NULLS)
    arresting_officer = models.ForeignKey(Officer, **NULLS)
    release_date = models.DateField(**NULLS)

    # 5000 since an unlimited number need to be supported
    aliases = models.CharField(max_length=5000, **NULLS)

    mugshot = models.ImageField(verbose_name='mug shot', **NULLS)
    gang = models.ForeignKey(Gang, **NULLS)

    sex = models.CharField(max_length=30, **NULLS)
    birth_date = models.DateField(**NULLS)

    prison_cell = models.ForeignKey(PrisonCell, **NULLS)
    # Address Fields
    phone_number = models.CharField(max_length=30, **NULLS)
    alt_phone_number = models.CharField(max_length=30, **NULLS)
    street_number = models.IntegerField(**NULLS)
    street_name = models.CharField(max_length=100, **NULLS)
    apartment_number = models.IntegerField(**NULLS)
    city = models.CharField(max_length=100, **NULLS)
    state = models.CharField(max_length=30, default='CA', **NULLS)
    zip_code = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=30, default='USA', **NULLS)

    temporary_street_number = models.IntegerField(**NULLS)
    temporary_street_name = models.CharField(max_length=100, **NULLS)
    temporary_apartment_number = models.IntegerField(**NULLS)
    temporary_city = models.CharField(max_length=100, **NULLS)
    temporary_state = models.CharField(max_length=30, default='CA', **NULLS)
    temporary_zip_code = models.IntegerField(**NULLS)
    temporary_country = models.CharField(max_length=30, default='USA', **NULLS)

    scars_marks_tattoos = models.TextField(**NULLS)
    medical_info = models.TextField(**NULLS)





    def __unicode__(self):
        return "inmate: {}".format(str(self.id))

    def time_to_release(self):
        if self.release_date is None:
            return
        now = datetime.datetime.now()
        return pd.Timestamp(self.release_date) - now


class MedicalRecord(models.Model):
    inmate = models.OneToOneField(Inmate)
    medical_file = models.FileField(**NULLS)

class FinancialRecord(models.Model):
    inmate = models.OneToOneField(Inmate)
    financial_file = models.FileField(**NULLS)


