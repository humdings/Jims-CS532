from django.db import models
import datetime

NULLS = dict(blank=True, null=True)


class PrisonFacility(models.Model):
    class Meta:
        verbose_name_plural = "Prision Facilities"

    name = models.CharField(max_length=100, **NULLS)
    phone_number = models.CharField(max_length=100, **NULLS)

    def __unicode__(self):
        return "{}".format(self.name)


class CellBlock(models.Model):
    facility = models.ForeignKey(PrisonFacility, **NULLS)
    block_number = models.IntegerField(**NULLS)

    def __unicode__(self):
        return "<CellBlock {}: {}>".format(self.block_number,
                                           self.facility.name)


class PrisonCell(models.Model):
    cell_block = models.ForeignKey(CellBlock, **NULLS)
    cell_number = models.IntegerField(**NULLS)
    bunk_a = models.ManyToManyField("Inmate", related_name="bunk_a", **NULLS)
    bunk_b = models.ManyToManyField("Inmate", related_name="bunk_b", **NULLS)

    def __unicode__(self):
        return "<Cell: {}, block: {}, facility: {}>".format(
            self.cell_number,
            self.cell_block.block_number,
            self.cell_block.facility
        )


class Gang(models.Model):
    name = models.CharField(max_length=100, **NULLS)
    rivals = models.ForeignKey('self', **NULLS)
    cell_blocks = models.ManyToManyField(CellBlock, **NULLS)

    def __unicode__(self):
        return "{}".format(self.name)


class Inmate(models.Model):
    # Name & Basic info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, **NULLS)
    social_secutity_number = models.IntegerField(**NULLS)

    release_date = models.DateField(**NULLS)

    # 5000 since an unlimited number need to be supported
    aliases = models.CharField(max_length=5000, **NULLS)

    mugshot = models.ImageField(verbose_name='mug shot', **NULLS)
    gang = models.ForeignKey(Gang, **NULLS)

    sex = models.CharField(max_length=30, **NULLS)
    birth_date = models.DateField(**NULLS)

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
        return "{}, {}, inmate id: {}".format(self.last_name, self.first_name, str(self.id))

    def time_to_release(self):
        now = datetime.datetime.now()
        return self.release_date - now
