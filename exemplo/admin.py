from django.contrib import admin

# Register your models here.
from exemplo.models import Pai, FilhoA, FilhoB


class FilhoAInline(admin.TabularInline):
    model = FilhoA


class FilhoBInline(admin.StackedInline):
    model = FilhoB


class PaiAdmin(admin.ModelAdmin):
    inlines = [
        FilhoAInline,
        FilhoBInline,
    ]


admin.site.register(Pai, PaiAdmin)
admin.site.register(FilhoA)
admin.site.register(FilhoB)
