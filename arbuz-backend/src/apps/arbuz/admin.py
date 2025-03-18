from django.contrib import admin
from .models import Forms, Project, News


class FormsAdmin(admin.ModelAdmin):
    pass
class NewsAdmin(admin.ModelAdmin):
    pass
class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Forms, FormsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Project, ProjectAdmin)