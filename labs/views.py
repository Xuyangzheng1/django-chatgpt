from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import json
import openai

# Create your views here.
def show_chat(response):
    """Show the main chat"""
    return render(response, "chat.html", {})

def operate_msg(request):
    """Send a request to OpenAI with a custom message"""

    msg =  request.GET.get('msg','')

    print("-------"+msg)
    
    openai.api_key = settings.OPENAI_KEY
    if settings.OPENAI_KEY != "":
        response = openai.Completion.create(
        # engine="code-davinci-002",
        engine = "text-davinci-003",
        prompt=msg,
        temperature=0,
        max_tokens=600,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=None
        )
    else:
        response = {'error': 'OpenAI key not configured'}
    print(json.dumps(response))
    return HttpResponse(json.dumps(response), content_type="application/json")
