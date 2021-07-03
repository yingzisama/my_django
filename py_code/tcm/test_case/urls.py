from django.urls import path , include

import test_case.views

urlpatterns = [
    path('index' , test_case.views.get_index_page)
]

