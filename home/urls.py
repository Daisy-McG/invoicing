from django.urls import path
from home.views import IndexView, PrivacyView


urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('privacy/', PrivacyView.as_view(), name="privacy"),
]