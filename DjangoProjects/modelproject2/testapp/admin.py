from django.contrib import admin
from testapp.models import Job , Book , Customer
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ['pdate' , 'location' , 'offeredsalary' , 'qualification'];

class BookAdmin(admin.ModelAdmin):
    list_display = ['bno' , 'title' , 'author' , 'publishdate'];

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name' , 'accno' , 'mailid' , 'phoneno' , 'age'];

admin.site.register(Job , JobAdmin);
admin.site.register(Book , BookAdmin);
admin.site.register(Customer , CustomerAdmin);