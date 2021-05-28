from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from .models import Email_store
from django.template.loader import render_to_string
from django.contrib import messages

def index(request):

    return render(request,'index.html')

def send_email(request):
    if request.method == 'POST': 
        email = request.POST.get('email', '')

        subject = "Welcome to EMOREC"
        message1 = render_to_string('emailTemplate.html')
        

        from_email= settings.EMAIL_HOST_USER
        if email is not None:
            
                
                Email_store_obj = Email_store(mEmail=email)
                Email_store_obj.save() 
                users_email=Email_store.objects.filter(mEmail=email).values('auto_increment_id')[0]['auto_increment_id']
                # users_email=Email_store.objects.filter(mEmail=email)
                print(users_email)
                unsub_link="http://127.0.0.1:8000/delete/{}/".format(users_email)
                message = "Dear user, Thank you for subscribing to the website.Click the attached link to unsubscribe. {}".format(unsub_link)
                send_mail(subject, message, from_email, [email])
                return render(request,'index.html.',{'email':email})
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
        
# def view_Email_lists(request):
#     list_of_Email= Email_store.objects.all()
    
#     context_variable = {
#         'emails':list_of_Email
#     }
#     return render(request,'ListOfEmails.html',context_variable)

def delete(request, ID):
    email_id = int(ID)
    try:
        email_sel = Email_store.objects.get(auto_increment_id = ID)
    except Email_store.DoesNotExist:
         return HttpResponse("Email not found!")
    email_sel.delete()
    return HttpResponse("You have been unsubscribed!!")
    
    #return HttpResponse("Record Deleted!!")