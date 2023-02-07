from .models import FullName, SchemaColum, Schema, CsvFile, Email, Date, Address, Text, CompanyName, PhoneNumber, DomainName, Job
from django.contrib import admin

# Register your models here.
admin.site.register(FullName)
admin.site.register(SchemaColum)
admin.site.register(Schema)
admin.site.register(CsvFile)
admin.site.register(Email)
admin.site.register(DomainName)
admin.site.register(PhoneNumber)
admin.site.register(CompanyName)
admin.site.register(Text)
admin.site.register(Address)
admin.site.register(Date)
admin.site.register(Job)
