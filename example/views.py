# example/views.py
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.utcnow()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current date is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
