
#Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime('%b %d, %Y - %H:%M hrs')
    return HttpResponse(f"Current server time is {now}")


def sort_numbers(request):
    # import pdb
    # pdb.set_trace()
    
    numbers = list()
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))
    
    data = {
        'status':'OK',
        'numbers': sorted(numbers),
        'message':'Numbers sorted successfully'
    }
    
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type="application/json"
    )

def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = f"Sorry {name} you are not allowed here!"
    else:
        message = f"Hello {name}! Welcome to Platzigram!"
        
    return HttpResponse(message)