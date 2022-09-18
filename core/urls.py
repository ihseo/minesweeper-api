from django.contrib import admin
from django.urls import path, include
from core.views import (GameList, NewGame, LeftClick, RightClick, LeftRightClick,)


urlpatterns = [
    path('games', GameList.as_view()),
    path('new_game', NewGame.as_view(), name='create_map'),
    path('left_click/<str:pk>', LeftClick.as_view(), name='left_click'),
    path('right_click/<str:pk>', RightClick.as_view(), name='right_click'),
    path('left_right_click/<str:pk>', LeftRightClick.as_view(), name='left_right_click'),
]