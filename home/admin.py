from django.contrib import admin
from home.models import datascience,webdev,python,Contact

# Register your models here.
admin.site.register(Contact)
admin.site.register(datascience)
admin.site.register(webdev)
admin.site.register(python)
