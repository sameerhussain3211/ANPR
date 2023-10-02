from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.Promo import ProcessingImg
from plateDetection.models import User
# Create your views here.

# result search
def plateView(request):
    return render(request,'addUserScreen.html')

# index --> default page
def index(request):
    users = User.objects.all()
    return render(request,'index.html', { 
        'users': users,
    })


# Screen navigation
def addUserScreen(request):
    return render(request, 'addUserScreen.html')


# Database adder
def addUsers(request):
    temp = request.POST
    user_name = temp.get('user_name')
    er = temp.get('erp')
    plate = temp.get('plate_num')
    prog = temp.get('program')
    
    new_user = User(student_name = user_name, erp = er, plate_num = plate, program = prog)
    new_user.save()
    print("post", new_user)
    return HttpResponseRedirect('/')

def getRecords(request):
    user = User.objects.all().filter(erp="25154")
    return render(request, 'individual_user.html',{
        'user': user[0],
    })

def individualDetails(request):
    temp = request.POST.get("address")
    img_process = ProcessingImg("test_images/" + temp + ".jpg")
    num_plate = img_process.process()
    
    
    #Filtering plate data from the image
    user = User.objects.all().filter(plate_num = num_plate.strip())
    
    # NUll check
    if len(user) >= 1:
        return render(request, 'individual_user.html',{
        "user" : user[0],  
        })
    else:
        return render(request, 'individual_user.html',{
            "user" : None,  
        })