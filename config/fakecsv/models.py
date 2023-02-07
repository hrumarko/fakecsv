from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Schema(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    column_separator = models.CharField(max_length=5)
    string_character = models.CharField(max_length=2)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.name}'
    

class SchemaColum(models.Model):
    column_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    from_int = models.IntegerField(null=True, blank=True)
    to_int = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(blank=True)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.column_name} - {self.schema}'
 

class CsvFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    date = models.DateField(default=timezone.now)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.title)


# class Type(models.Model):
#     name_of_type = models.CharField(max_length=255)
#     is_integer = models.BooleanField()
#     is_date = models.BooleanField()
#
#     def __str__(self):
#         return f'{self.name_of_type}'
#
#
class FullName(models.Model):
    full_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.full_name


class Email(models.Model):
    email = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.email


class DomainName(models.Model):
    domain = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.domain


class PhoneNumber(models.Model):
    phone = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.phone


class CompanyName(models.Model):
    company_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.company_name


class Text(models.Model):
    speech = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.speech


class Address(models.Model):
    address = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.address


class Date(models.Model):
    date = models.DateField(unique=True)


class Job(models.Model):
    job = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.job

