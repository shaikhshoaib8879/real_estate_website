from django.shortcuts import render,redirect
from .models import Contact
from django.core.mail import send_mail 
from django.contrib import messages

# Create your views here.
def contact(request):
    print(request.method)
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
        
        #check if user has enquiery
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"You already made a inquiry ,request for this listing")
                return redirect('/listings/'+listing_id)
            
            
        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        
        contact.save()
        
        #send_mail
        
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for' + listing + '.Sign into the admin panel for more info',
            'shoaib.shaikh@mirraw.com',
            [realtor_email,'tech@gmail.com'],
            fail_silently=False
            
            
        )
        messages.success(request,"Your request have been Submitted ")
        return redirect('/listings/'+listing_id)