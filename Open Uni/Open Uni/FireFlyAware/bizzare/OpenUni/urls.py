from .import views
from django.urls import path
app_name  = 'OpenUni'
# urlpatterns = [
#     # ex: /polls/
#     path("", views.index, name="index"),
#     # ex: /polls/5/
#     path("<int:category_id>/", views.detail, name="detail"),
#     # ex: /polls/5/results/
#     path("<int:category_id>/homepage/", views.homepage, name="homepage"),
#     # ex: /polls/5/vote/
#     path("<int:category_id>/menu/", views.menu, name="menu"),
# ]

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.Menu, name="menu"),
]