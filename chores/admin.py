from django.contrib import admin

# Register your models here.

from .models import ChoreList, Chore

# Las clases inline sirven para que podamos relacionar el objeto contenedor con los objetos contenidos
# (En este caso desde un objeto ChoreList podemos ver los Chore asociados)
# El extra = 3 sirve para que nos muestre por defecto 3 objetos Chore
class ChoreInLine(admin.TabularInline):
    model = Chore
    extra = 3

# This class is used to modify how we show the ChoreList
# objects from the admin perspective. In this particular
# case we are changing the order of the attributes
class ChoreListAdmin(admin.ModelAdmin):

    # In this particular case we are changing the order of the attributes
    #fields = ['due_date', 'name']

    # With fieldsets we can divide the ChoreList creation screen in different sections
    # (Title of the section, content)
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date Info', {'fields': ['due_date']})
    ]
    inlines = [ChoreInLine]

admin.site.register(ChoreList, ChoreListAdmin)
admin.site.register(Chore)