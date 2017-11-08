from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from HKDataBase.models import HKData
from HKDataBase.serializers import HKDataSerializer
from HKDataBase.pagination import DataPagination

# Create your views here.


class HKDataList(generics.ListAPIView):
    queryset = HKData.objects.all()
    serializer_class = HKDataSerializer
    pagination_class = DataPagination

@api_view(['GET','POST'])
def hkdata_list(request,format = None):
    if(request.method == 'GET') :
        datalist = HKData.objects.all()
        serializer = HKDataSerializer(datalist,many = True,context={'request':request})
        return Response(DataPagination(serializer.data))