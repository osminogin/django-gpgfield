from django.db import models
from pgpfield.fields import PGPField


class PGPFieldTestModel(models.Model):
    pgp = PGPField("test", null=True, blank=True)

    class Meta:
        app_label = 'pgpfield'


class PGPFieldWithDefaultTestModel(models.Model):
    pgp = PGPField(default={"sukasuka": "YAAAAAZ"})

    class Meta:
        app_label = 'pgpfield'


class BlankPGPFieldTestModel(models.Model):
    null_pgp = PGPField(null=True)
    blank_pgp = PGPField(blank=True)

    class Meta:
        app_label = 'pgpfield'


class CallableDefaultModel(models.Model):
    pgp = PGPField(default=lambda: {'x': 2})

    class Meta:
        app_label = 'pgpfield'
