from django.contrib import admin

from .models import Consultes
from .models import Bases
from .models import Respostes
from .models import Solucions

admin.site.register(Consultes)
admin.site.register(Bases)
admin.site.register(Respostes)
admin.site.register(Solucions)