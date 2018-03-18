from django.contrib import admin

from .models import Game, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('game', 'rating', 'user_name', 'comment', 'comment_date')
    list_filter = ['comment_date', 'user_name']
    search_fields = ['comment']
    
admin.site.register(Game)
admin.site.register(Review, ReviewAdmin)
