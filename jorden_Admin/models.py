from django.db import models
from froala_editor.fields import FroalaField
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class ListOfCompanies(models.Model):
    company_id=models.CharField(max_length=50)
    company_name=models.CharField(max_length=75)
    company_password=models.CharField(max_length=75)

class PendingActionable(models.Model):
    point = models.CharField(max_length=100)
    clientRemarks = models.CharField(max_length=500, blank=True)
    status = models.BooleanField(default=False, blank=True)
    company=models.ForeignKey(ListOfCompanies,related_name='PendingActions',on_delete=models.CASCADE)

class WatchOutPoint(models.Model):
    point = models.CharField(max_length=100)
    clientRemarks = models.CharField(max_length=500, blank=True)
    company=models.ForeignKey(ListOfCompanies,related_name='WatchOutPoint',on_delete=models.CASCADE)
  
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=100)
    industry_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    company_email = models.CharField(max_length=30, null=True)
    gst_number = models.CharField(max_length=20)
    pan_number = models.CharField(max_length=20)
    pf_number = models.CharField(max_length=20, null=True)
    esic_number = models.CharField(max_length=20, null=True)
    company=models.ForeignKey(ListOfCompanies,related_name='Companie',on_delete=models.CASCADE)

class CompanyAddress(models.Model):
    company=models.ForeignKey(ListOfCompanies,related_name='CompanyAddress',on_delete=models.CASCADE)
    address_line = models.TextField()
    locality = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pin_code = models.CharField(max_length=6)

class CompanyContext(models.Model):
    company=models.ForeignKey(ListOfCompanies,related_name='CompanyContext',on_delete=models.CASCADE)
    about_company=FroalaField(theme='gray', blank=True, null=True)
    what_company=FroalaField(theme='gray', blank=True, null=True)
    key_info=FroalaField( theme='gray',blank=True, null=True)
    any_specific=FroalaField(theme='gray', blank=True, null=True)


class BankDetail(models.Model):
    company=models.ForeignKey(ListOfCompanies,related_name='BankDetail',on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=15)
    ifsc_code = models.CharField(max_length=15)
    location = models.CharField(max_length=50)


class Rule(models.Model):
    name = models.CharField(max_length=200)

class Channel(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=100)
    rule = models.ForeignKey(Rule, related_name='channels',on_delete=models.CASCADE, blank=True)