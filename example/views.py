# example/views.py
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.utcnow()

    def ask():
        name = input("What is the name of your team? ")
        return f'''<p>The current date is { name }.</p>'''

    html = f'''
    <html>
        <body>
            <h1>FIFA Road to Glory Career Mode Tracker</h1>
            <p>The current date is { ask }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
