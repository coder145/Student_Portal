from django.contrib import admin

# Register your models here.
from .models import MatricNumber, Department, HashedPasword

class DepartmentInline(admin.StackedInline):
    model = Department
    extra = 1

class Password(admin.StackedInline):
    model = HashedPasword
    extra = 1

class MatricNumberAdmin(admin.ModelAdmin):
    fieldsets = [
        ("student name",{"fields": ["first_name","Last_name","level","matricnumber"]}),
        

    ]
    inlines = [DepartmentInline,Password]
    pass

admin.site.register(MatricNumber, MatricNumberAdmin)

