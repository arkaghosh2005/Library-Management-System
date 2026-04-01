from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('books/', views.book_table, name='book_table'),
    path('book/add/', views.book_add, name='book_add'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('book/<int:book_id>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:book_id>/delete/', views.book_delete, name='book_delete'),

    path('users/', views.user_table, name='user_table'),
    path('user/add/', views.user_add, name='user_add'),
    path('user/<int:user_id>/', views.user_details, name='user_details'),
    path('user/<int:user_id>/edit/', views.user_edit, name='user_edit'),
    path('user/<int:user_id>/delete/', views.user_delete, name='user_delete'),

    path('records/open/', views.records_open, name='records_open'),
    path('records/closed/', views.records_closed, name='records_closed'),
    path('records/borrow/', views.records_borrow, name='records_borrow'),
    path('return/<int:record_id>/', views.return_book, name='return_book'),
    path('reissue/<int:record_id>/', views.reissue_book, name='reissue_book'),
]