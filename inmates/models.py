from django.db import models




NULLS = dict(blank=True, null=True)


class Inmate(models.Model):
    # Name & Basic info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, **NULLS)
    social_secutity_number = models.IntegerField(**NULLS)
    # 5000 since an unlimited number need to be supported
    aliases = models.CharField(max_length=5000, **NULLS)

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


    def __unicode__(self):
        return "{}, {}, inmate id: {}".format(self.last_name, self.first_name, str(self.id))