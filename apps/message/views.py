from django.shortcuts import render
from apps.message.models import UserMessage

def getform(request):
    usermessage = UserMessage()
    if request.method == 'POST':
        usermessage.name = request.POST.get('name','')
        usermessage.email = request.POST.get('email','')
        usermessage.address = request.POST.get('address','')
        usermessage.message = request.POST.get('message','')
        usermessage.object_id = 't'
        usermessage.save()

    return render(request,'message_form.html')
