from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .database import search_in


@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    try:
        req = request.query_params['id']
        results = search_in(req)
        print(results)
        item_name = results[0]
        valid_until = results[1]
        price = results[2]


        return Response({'message': "we received your request", 'item name': item_name, 'price': price, 'valid until': valid_until})
    except:
        return Response({'message': "Not in data base"})

     