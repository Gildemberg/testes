from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return JsonResponse(
        {"message": "Aplicação Programação Avançada - qualidade_software - OK"}
    )


@csrf_exempt
def soma(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Use POST'}, status=405)
    
    try:
        data = json.loads(request.body)
    except Exception:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    
    a = data.get('a')
    b = data.get('b')
    
    try:
        a = float(a)
        b = float(b)
    except Exception:
        return JsonResponse({'error': 'a e b devem ser números'}, status=400)
    
    return JsonResponse({'resultado': a + b})