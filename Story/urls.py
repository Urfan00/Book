from django.urls import path
from Story.views import story


urlpatterns = [
    path('story_list/', story, name='story_list'),
]
