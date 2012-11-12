from django.contrib import admin

from blog.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'colored_status')

    def colored_status(self, modelEntry):
        status_str = modelEntry.get_status_display()
        #http://docs.djangoproject.com/en/dev/ref/models/instances/#django.db.models.Model.get_FOO_display
        color_str = "Black"
        if modelEntry.status == modelEntry.LIVE_STATUS: color_str = "Green"
        elif modelEntry.status == modelEntry.DRAFT_STATUS: color_str = "Red"
        elif modelEntry.status == modelEntry.HIDDEN_STATUS: color_str = "Gray"
        return '<span style="color: %s;">%s</span>' % (color_str, status_str)
    colored_status.allow_tags = True
    colored_status.admin_order_field = 'status'


admin.site.register(Entry, EntryAdmin)


