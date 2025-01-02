# hanasu/urls.py
from django.urls import path
from hanasu import views

urlpatterns = [
    path("", views.home, name='home'),
    path("hiragana/", views.hiragana, name='hiragana'),
    path("katakana/", views.katakana, name='katakana'),
    path("lesson0/", views.lesson0, name='lesson0'),
    path("lesson0/numbersquiz/", views.numbers_quiz, name='numbers_quiz'),
    path("lesson0/numbersquiz/<int:question_number>/", views.numbers_quiz, name='numbers_quiz'),
    path("lesson0/greetingsquiz/", views.greetings_quiz, name='greetings_quiz'),
    path("lesson0/greetingsquiz/<int:question_number>/", views.greetings_quiz, name='greetings_quiz'),
    path("lesson1/", views.lesson1, name='lesson1'),
    path('hiragana/quiz/<int:question_number>/', views.hiragana_quiz, name='hiragana_quiz'),
    path('hiragana/quiz/', views.hiragana_quiz, name='hiragana_quiz'),  # Default to question 1
    path('katakana/quiz/<int:question_number>/', views.katakana_quiz, name='katakana_quiz'),
    path('katakana/quiz/', views.katakana_quiz, name='katakana_quiz'), 
]
