from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name=''),
    path('category', views.category_list, name='category_list'),
    path('deleted-categories', views.deleted_category_list, name='deleted_category_list'),
    path('add-category', views.add_category, name='add_category'),
    path('save-category', views.save_category, name='save_category'),
    path('edit-category/<int:id>', views.edit_category, name='edit_category'),
    path('update-category', views.update_category, name='update_category'),
    path('delete-category/<int:id>', views.delete_category, name='delete_category'),
    path('restore-category/<int:id>', views.restore_category, name='restore_category'),
    path('permanent-delete-category/<int:id>', views.permanent_delete_category, name='permanent_delete_category'),
    
    path('product', views.product_list, name='product_list'),
    path('deleted-products', views.deleted_product_list, name='deleted_product_list'),
    path('add-product', views.add_product, name='add_product'),
    path('save-product', views.save_product, name='save_product'),
    path('edit-product/<int:id>', views.edit_product, name='edit_product'),
    path('update-product', views.update_product, name='update_product'),
    path('delete-product/<int:id>', views.delete_product, name='delete_product'),
    path('restore-product/<int:id>', views.restore_product, name='restore_product'),
    path('permanent-delete-product/<int:id>', views.permanent_delete_product, name='permanent_delete_product'),
]
