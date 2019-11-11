from django.urls import include, path
from crud import views

app_name = 'crud'

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.addForm, name="add-form-product"),
    path('save', views.save, name='save-add-product'),
    path('<int:id>', views.show, name='show-product'),
    path('edit/<int:id>', views.editForm, name='edit-form-product'),
    path('save-edit/<int:id>', views.saveEdit, name='save-edit-product'),
    path('delete/<int:id>', views.deleteForm, name='delete-form-product'),
    path('delete-confirm/<int:id>', views.deleteConfirmation, name='delete-confirmation-product'),
    path('addClass', views.addClassForm, name="add-class-form-product"),
    path('saveClass', views.saveClass, name='save-class-add-product'),
]
