
#Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime('%b %d, %Y - %H:%M hrs')
    return HttpResponse(f"Current server time is {now}")


def hi(request):
    # import pdb
    # pdb.set_trace()
    
    numbers = list()
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))
    
    obj = dict()
    obj['numbers'] = sorted(numbers)
    
    return HttpResponse(json.dumps(obj))
