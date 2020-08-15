from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
# Utilities
from datetime import datetime
import json
from routing.apps.routes import controller


# Create your views here.
@csrf_exempt
def routing_view(request):
    data = []
    if request.method == 'POST':
        req = json.loads(request.body)
        try:
            obj = {
                "matrix": req['matrix'],
                "max_vehicles": req['max_vehicles']
            }
            res = controller.main(obj)
            print(res)
            data.append({
                "routes": res['routes'],
                "map_url": res['map_url']
            })
        except:
            pass
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")