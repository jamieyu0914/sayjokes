from rest_framework.response import Response
from api import data_utils
from .data_utils import getData
from rest_framework.response.decoractors import api_view

@api_view(['GET'])
def getData(requset):
    person = {'name':'Jamie', 'age':26}
    return Response(person)

