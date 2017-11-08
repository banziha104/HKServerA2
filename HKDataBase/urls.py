from django.conf.urls import url
from .models import HKData
from HKDataBase import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$',views.HKDataList.as_view()),
]
