from django.contrib import admin
from jorden_Admin.models import *
# Register your models here.
class PendingActionableAdmin(admin.TabularInline):
    model = PendingActionable
class WatchOutPointAdmin(admin.TabularInline):
    model = WatchOutPoint

class CompanyAdmin(admin.TabularInline):
    model = Company
class CompanyAddressAdmin(admin.TabularInline):
    model = CompanyAddress


class CompanyContextAdmin(admin.TabularInline):
    model = CompanyContext
class BankDetailAdmin(admin.TabularInline):
    model = BankDetail 



class ListOfCompaniesAdmin(admin.ModelAdmin):
    inlines=[PendingActionableAdmin,WatchOutPointAdmin,CompanyAdmin,CompanyAddressAdmin,CompanyContextAdmin,BankDetailAdmin,]
    list_display=('company_id','company_name')

admin.site.register(ListOfCompanies,ListOfCompaniesAdmin)
class ChannelAdmin(admin.TabularInline):
    model = Channel

class RuleAdmin(admin.ModelAdmin):
   inlines = [ChannelAdmin,]

admin.site.register(Rule,RuleAdmin)
