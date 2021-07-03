from django.shortcuts import render

from django.http import HttpResponse

from test_case.models import test_case_management
# Create your views here.


def get_index_page(request):
    all_case = test_case_management.objects.all()
    return render(request, 'test_case/index.html',
                    {
                        'case_management_list': all_case
                    }
                )