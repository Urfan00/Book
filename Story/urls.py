from django.urls import path
from Story.views import StoryList, story, story_detail


urlpatterns = [
    path('story_list/', StoryList.as_view(), name='story_list'),
    path('story_detail/<int:id>', story_detail, name='story_detail'),
]
