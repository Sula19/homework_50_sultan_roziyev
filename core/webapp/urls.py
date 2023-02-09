from django.urls import path
from webapp.views.add import add_view
from webapp.views.stats import view_cat

urlpatterns = [
    path('', add_view),
    path('cat_stats/', view_cat, name='view')
]
