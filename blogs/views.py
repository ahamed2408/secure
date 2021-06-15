from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import orderss, shipd
from datetime import datetime,date
from django.core.mail import send_mail
import datetime
from django import template


def registers(request):
    context = {
        'des': orderss.objects.last(),
        'shi':shipd.objects.all()
    }

    contexts=context['des']
    contextss=context['shi']
    msg=0
    for i in contextss:
        if((contexts.orgin==i.shorig) and (contexts.dest==i.shdest)):
            if(contexts.t_g=="Eatables" and i.con_e<200 and contexts.date<i.shdate):
                msg=1
            elif(contexts.t_g=="Solids" and i.con_s<200 and contexts.date<i.shdate):
                msg=1
            elif(contexts.t_g=="Fluids" and i.con_f<200 and contexts.date<i.shdate):
                msg=1

            if(msg==1):
                contexts.shipid=i.shipid
                contexts.save()
                contexts.rej=0
                contexts.save()
                break



    if(contexts.rej==1):
        contexts.cost=0
        contexts.save()
        contexts.nodays=0
        contexts.save()
    

    if request.method=='POST':
        context = {
            'des': orderss.objects.last(),
            'shi':shipd.objects.all()
        }

        contexts=context['des']
        contextss=context['shi']


        sa=request.POST.get('ship_avai')
        se=request.POST.get('sem')


        



#Condition for Eatabale Conatiner
        
        for i in contextss:
            ass=i.shdate
            if(str(ass)==sa):
                if((contexts.orgin==i.shorig) and (contexts.dest==i.shdest)):
                    if(contexts.t_g=="Eatables"):
                        i.con_e+=contexts.weight
                        i.save()
                        contexts.rej=0
                        contexts.save()
                    elif(contexts.t_g=="Solids"):
                        i.con_s+=contexts.weight
                        i.save()
                        contexts.rej=0
                        contexts.save()
                    elif(contexts.t_g=="Fluids"):
                        i.con_f+=contexts.weight
                        i.save()
                        contexts.rej=0
                        contexts.save()

                    contexts.shipid=i.shipid
                    contexts.save()
        
        if(contexts.rej==0):
            mrs='Order Confirmation'
            mrb="Thanks for your order with SeaLanes. We hereby confirm the same. Below are the details of your order : \n\nDate of Order: " +str(contexts.date)+"\nSender & Address: "+ contexts.sen_name+" , "+contexts.sen_add +"\nReceiver & Address: "+contexts.rec_name+" ,"+contexts.rec_add+ "\nType of Goods: "+ contexts.t_g +"\nWeight of Goods: " + str(contexts.weight)+" kgs." +"\nCost: $"+str(contexts.cost)+"\nOrigin: "+contexts.orgin+"\nDestination : "+contexts.dest+"\nPriority: "+contexts.pri +"\n\n\n\nPlease contact our support team at +98 7550112345 for further queries.\nThank you,\nTeam SeaLanes."  
            send_mail(mrs,mrb,'SeaLanes Shipping <noreplysealanes@gmail.com>',[se],fail_silently=False,)
        else:
            mrs='Regrets - Order delayed'
            mrb="We regret to inform you that your order with SeaLanes has been delayed due to full capacity in all the ships for the month.\nWe will return back the package to your address within two working days."+"\n\n" + "If you have any queries, please contact our support team at +98 7550112345." + "\n\nThank you,\nTeam SeaLeanes."
            send_mail(mrs,mrb,'SeaLanes Shipping <noreplysealanes@gmail.com>',[se],fail_silently=False,)

    
        dess=orderss.objects.last()
        act=1
        return render(request, 'blogs/register-2.html',{'dess':dess,'sa':sa,'act':act})

    return render(request, 'blogs/register-2.html', {'contexts':contexts,'contextss':contextss,'m':msg})

def front(request):
    return render(request, 'blogs/frontship.html')


def dash_two(request):
    return render(request, 'blogs/dashboard-2.html')


def free_ship(request):
    contextss=shipd.objects.all()
    cd=date.today()
    cd=str(cd)
    if request.method=='POST':

        shf=request.POST.get('shipid')
        shf=int(shf)
        c=request.POST.get('confirm')
        d=request.POST.get('dates')
        d=datetime.datetime.strptime(d, '%Y-%m-%d').date()
        context = shipd.objects.get(shipid=shf)
        print("shf: ",shf," type: ",type(shf))
        print("c: ",c," type: ",type(c))
        print("d: ",d," type: ",type(d))
        print(context.con_e)
        print(context.con_f)
        print(context.con_s)
        cd=date.today()
        cd=str(cd)
        print("cd: ",cd," type: ",type(cd))
        print("cd: ",cd," type: ",type(cd))
        if(shf==context.shipid and c=="Yes"):
            context.shdate=d
            context.save()
            context.con_e=0
            context.save()
            context.con_f=0
            context.save()
            context.con_s=0
            context.save()


        return render(request, 'blogs/free.html',{'contextss':contextss,'cd':cd,'num':range(1,49)})
    return render(request, 'blogs/free.html',{'contextss':contextss,'cd':cd,'num':range(1,49)})




    
    return render(request, 'blogs/free.html',{'contextss':contextss,'cd':cd,'num':range(1,49)})


def home(request):

    mrs='Order Confirmation'
    mrb="This is an automated Message"
    #send_mail(mrs,mrb,'SeaLanes Shipping <noreplysealanes@gmail.com>',['ahamed.irshad24@gmail.com','ashwinkumar.cse_a2017@crescent.education','gregory.cse_a2017@crescent.education'],fail_silently=False,)
    context = {
        'des': orderss.objects.all(),
        'shi':shipd.objects.all()
    }
    contexts=context['des']
    contextss=context['shi']
    return render(request, 'blogs/home.html', {'contexts':contexts,'contextss':contextss})


def add(request):
    context = {
        'des': orderss.objects.all(),
        'shi':shipd.objects.all()
    }
    contexts=context['des']
    contextss=context['shi']
    
    if request.method=='POST':
        se=request.POST.get('sem')
        se=str(se)
        re=request.POST.get('rem')
        re=str(re)
        sen_n = request.POST.get('sen_name')
        sen_a = request.POST.get('sen_add')
        sen_p = request.POST.get('sen_ph')
        rec_n = request.POST.get('rec_name')
        rec_a = request.POST.get('rec_add')
        rec_p = request.POST.get('rec_ph')
        tg = request.POST.get('t_g')
        w = request.POST.get('weight')
        org = request.POST.get('orgin')
        d = request.POST.get('dest')
        p = request.POST.get('pri')

        context = {
        'des': orderss.objects.all(),
        'shi':shipd.objects.all()
        }
        contexts=context['des']
        contextss=context['shi']

        

#Date  today

        today=date.today()
        d1=today.strftime("%d")
        d1=str(d1)
        d2=today.strftime("%b")
        d2=str(d2)
        d3=today.strftime("%Y")
        d3=str(d3)
        d4=today.strftime("%A")
        d4=str(d4)

        d5=d1+"-"+d2+"-"+d3
        



#condition for calculating the distance
        if org=="Miami":
            t1=1
        elif org=="Cape Town":
            t1=2
        elif org=="Chennai":
            t1=3
        elif org=="Osaka":
            t1=4
        
        if d=="Miami":
            t2=1
        elif d=="Cape Town":
            t2=2
        elif d=="Chennai":
            t2=3
        elif d=="Osaka":
            t2=4


        shipsd=abs(t1-t2)+4
        c=0
        ro=1


#Condition for cost
        if(shipsd==5):
            c=20
        if(shipsd==6):
            c=30
        if(shipsd==7):
            c=40

#Urgent Condition
        if p=="Urgent":
            shipsd-=1
            c+=2

#cost increment based on weight
        w=int(w)
        if(w>=0 and w<=25):
            c+=2
        elif(w>=26 and w<=50):
            c+=4
        elif(w>=51 and w<=75):
            c+=6
        elif(w>=76 and w<=100):
            c+=8

        sid=1



#################################Consignment Allocation to the right Container#####################################



#Email for Sender And Reciever
       # if(ro==1):
        #    mrs='Regrets - Order delayed'
         #   mrb="We regret to inform you that your order with SeaLanes has been delayed due to full capacity in the ship." +"\n" + "However, your order will be dispatched in the next ship, a week later." +"\n\n" + "If not okay with this, please contact our support team at +98 7550112345." + "\n\nThank you,\nTeam SeaLeanes."

          #  send_mail(mrs,mrb,'SeaLanes Shipping <noreplysealanes@gmail.com>',[se],fail_silently=False,)
       # else:
        #    mrs='Order Confirmation'
         #   mrb="Thanks for your order with SeaLanes. We hereby confirm the same. Below are the details of your order : \n\nDate of Order: " +d5+"\nSender & Address: "+ sen_n+" , "+sen_a +"\nReceiver & Address: "+rec_n+" ,"+rec_a+ "\nType of Goods: "+ tg +"\nWeight of Goods: " + str(w) +" kgs." +"\nCost: $"+str(c)+"\nOrigin: "+org+"\nDestination : "+ d+"\nPriority: "+p +"\n\n\n\nPlease contact our support team at +98 7550112345 for further queries.\nThank you,\nTeam SeaLanes."
              
          #  send_mail(mrs,mrb,'SeaLanes Shipping <noreplysealanes@gmail.com>',[se],fail_silently=False,)
        
        x=orderss(sen_name = sen_n , sen_add = sen_a , sen_ph = sen_p ,rec_name = rec_n , rec_add = rec_a , rec_ph = rec_p , t_g = tg, orgin = org, dest = d, pri = p, nodays=shipsd, weight=w,  rej=ro, cost=c, shipid=sid,dd=d1,dm=d2,dy=d3,ddd=d4)
        x.save()

        return redirect('blogs-register-2')
        return render(request, 'blogs/register-2.html')
    else:
        return render(request, 'blogs/register.html',{'contexts':contexts,'contextss':contextss})

def dashboard(request):
    #student_obj = Desii.objects.get(id=Desii.objects.last().id)
    #student_obj.cost= 710
    #student_obj.save()
# For paasing the weight of goods in chartJS
    a=shipd.objects.all().delete()
    return render(request, 'blogs/dashboard.html')


    '''
    Temporary Function for last object function
    def add(request):
    if request.method=='POST':
        sen_n = request.POST.get('sen_name')
        sen_a = request.POST.get('sen_add')
        sen_p = request.POST.get('sen_ph')
        rec_n = request.POST.get('rec_name')
        rec_a = request.POST.get('rec_add')
        rec_p = request.POST.get('rec_ph')
        tg = request.POST.get('t_g')
        org = request.POST.get('orgin')
        d = request.POST.get('dest')
        p = request.POST.get('pri')
        shi=Des.objects.last()
        if tg==shi.t_g:
            ship=500
        else:
            ship=10
        x=Des(sen_name = sen_n , sen_add = sen_a , sen_ph = sen_p ,rec_name = rec_n , rec_add = rec_a , rec_ph = rec_p , t_g = tg , orgin = org, dest = d, pri = p,shipment=ship)
        x.save()

    return render(request, 'blog/register.html', {'title': 'About'})






    Temporary Function for sum function

    def add(request):
    if request.method=='POST':
        sen_n = request.POST.get('sen_name')
        sen_a = request.POST.get('sen_add')
        sen_p = request.POST.get('sen_ph')
        rec_n = request.POST.get('rec_name')
        rec_a = request.POST.get('rec_add')
        rec_p = request.POST.get('rec_ph')
        tg = request.POST.get('t_g')
        org = request.POST.get('orgin')
        d = request.POST.get('dest')
        p = request.POST.get('pri')
        shi=Des.objects.all()
        tp=sum(shi.values_list('shipment',flat=True))
        if tg=="Eatable":
            ship=5
        else:
            ship=10
        x=Des(sen_name = sen_n , sen_add = sen_a , sen_ph = sen_p ,rec_name = rec_n , rec_add = rec_a , rec_ph = rec_p , t_g = tg , orgin = org, dest = d, pri = p,shipment=tp)
        x.save()

    return render(request, 'blog/register.html', {'title': 'About'})
    '''
    
    
    '''
     <div class="col-md-8">
    <canvas id="myChart" width="400" height="400"></canvas>
<script>
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels:['Mad','Mum','Bang'] ,
        datasets: [{
            label: 'Types of Goods',
            data: [{% for dess in des %} {{ dess.shipment}}, {% endfor %}],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
</script>
</div>

<div class="col-md-4">
    <canvas id="myChart" width="400" height="400"></canvas>
<script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels:['Mad','Mum','Bang'] ,
            datasets: [{
                label: 'Types of Goods',
                data: [{% for dess in des %} {{ dess.shipment}}, {% endfor %}],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    </script>
</div>
    '''