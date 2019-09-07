from django.contrib import admin
# Register your models here.
from .models import extenduser
from .models import serviceprovider
from .models import Experties
from .models import Orders
from .models import Incidence




admin.site.register(extenduser)
admin.site.register(serviceprovider)
admin.site.register(Experties)
admin.site.register(Orders)
admin.site.register(Incidence)
