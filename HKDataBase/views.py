from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from HKDataBase.models import HKData
from HKDataBase.serializers import HKDataSerializer
# Create your views here.

@api_view(['GET','POST'])
def hkdata_list(request,format = None):
    if(request.method == 'GET') :
        datalist = HKData.objects.all()
        serializer = HKDataSerializer(datalist,many = True)
        return Response(serializer.data)

