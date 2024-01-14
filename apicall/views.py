from django.http import JsonResponse
from rest_framework.decorators import api_view



@api_view(['GET', 'POST'])
def n2_sender(request):
    return JsonResponse({"message":"dcefd"})