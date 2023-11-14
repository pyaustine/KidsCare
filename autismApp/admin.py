from django.contrib import admin
from . models import Result

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('age',
                    'sex',
                    'a1',
                    'a2',
                    'a3',
                    'a4',
                    'a5',
                    'a6',
                    'a7',
                    'a8',
                    'a9',
                    'a10',
                    'jaundice',
                    'asd_history',
                    'test_completed_by',
                    'outcome',
                    'date'
                    )

admin.site.register(Result, DataAdmin)