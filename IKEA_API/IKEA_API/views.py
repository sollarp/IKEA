from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .database import search_in


@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    req = request.query_params['id']
    results = search_in(req)
    print(f" teremtes {request.query_params['id']}")


    return Response({'message': "we received your request", 'result': results})
     
