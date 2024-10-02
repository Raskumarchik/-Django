"""Определяет схемы URL для learning_logs."""

from django.urls import path
from .import views
from django.contrib.auth import views as authViews


app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех тем.
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path ('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница для добавляния новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница для добавления новой записи
    path ('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страница для редактирования записей
    path ('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('exit/',authViews.LogoutView.as_view(), name='exit'),


]