from django.urls import path
from Story.views import story, story_detail


urlpatterns = [
    path('story_list/', story, name='story_list'),
    path('story_detail/<int:id>', story_detail, name='story_detail'),
]
