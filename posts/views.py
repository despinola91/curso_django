# Django
from django.shortcuts import render
from django.http import HttpResponse

# Utilities
from datetime import datetime

# Create your views here.

posts = [
    
    {
        'name': 'Mont Blac',
        'user':'Yesica Cortes',
        'timestamp': datetime.now().strftime('%b %d, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200?image=1036'
    },
    {
        'name': 'Via Lactea',
        'user':'Dario Espinola',
        'timestamp': datetime.now().strftime('%b %d, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200?image=903'
    },
    {
        'name': 'Nuevo auditorio',
        'user':'testing',
        'timestamp': datetime.now().strftime('%b %d, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200?image=1076'
    },
]

def list_posts(request):
    """List existing posts."""
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
