from django.shortcuts import render
from jorden_Admin.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import urllib
# Create your views here.

def admin(request):
    return render(request,'admin_home.html')

# def fb(request):
#         data = {
#         'j_username': '949172070',
#         'j_password': 'ap16bv1833'
#         }

#         response = requests.post(
#             'www.facebook.com/login',
#             data=data
#         )
        
#         r = requests.post("https://www.facebook.com/login/",data=urllib.urlencode({'username': '9491728070', 'j_password': 'ap16bv1833'}))
#         print(r.text)
#         # print(response)
#         return render(request,'admin.html')


class List_of_companies(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self,request,format=None):
        List_Of_Companies=ListOfCompanies.objects.all().values()
        return Response(List_Of_Companies)


class About_a_company(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self,request,pk,format=None):
        List_Of_Companies=ListOfCompanies.objects.filter(company_id=pk).values()
        return Response(List_Of_Companies)

