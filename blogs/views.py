from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import analytics, orderss, shipd
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
    a1d=datetime.date(2021,6,3)
    a2d=datetime.date(2021,6,9)
    a3d=datetime.date(2021,6,15)
    a4d=datetime.date(2021,6,21)
    a1=shipd(shipid=1,shname='MCP-101',shorig='Miami',shdest='Cape Town',shdate=a1d,con_e=0,con_f=0,con_s=0)
    a1.save()
    a2=shipd(shipid=2,shname='MCP-102',shorig='Miami',shdest='Cape Town',shdate=a2d,con_e=0,con_f=0,con_s=0)
    a2.save()
    a3=shipd(shipid=3,shname='MCP-103',shorig='Miami',shdest='Cape Town',shdate=a3d,con_e=0,con_f=0,con_s=0)
    a3.save()
    a4=shipd(shipid=4,shname='MCP-104',shorig='Miami',shdest='Cape Town',shdate=a4d,con_e=0,con_f=0,con_s=0)
    a4.save()


    b1d=datetime.date(2021,6,4)
    b2d=datetime.date(2021,6,10)
    b3d=datetime.date(2021,6,16)
    b4d=datetime.date(2021,6,22)
    b1=shipd(shipid=5,shname='MCH-101',shorig='Miami',shdest='Chennai',shdate=b1d,con_e=0,con_f=0,con_s=0)
    b1.save()
    b2=shipd(shipid=6,shname='MCH-102',shorig='Miami',shdest='Chennai',shdate=b2d,con_e=0,con_f=0,con_s=0)
    b2.save()
    b3=shipd(shipid=7,shname='MCH-103',shorig='Miami',shdest='Chennai',shdate=b3d,con_e=0,con_f=0,con_s=0)
    b3.save()
    b4=shipd(shipid=8,shname='MCH-104',shorig='Miami',shdest='Chennai',shdate=b4d,con_e=0,con_f=0,con_s=0)
    b4.save()

    c1d=datetime.date(2021,6,5)
    c2d=datetime.date(2021,6,11)
    c3d=datetime.date(2021,6,17)
    c4d=datetime.date(2021,6,23)
    c1=shipd(shipid=9,shname='MO-101',shorig='Miami',shdest='Osaka',shdate=c1d,con_e=0,con_f=0,con_s=0)
    c1.save()
    c2=shipd(shipid=10,shname='MO-102',shorig='Miami',shdest='Osaka',shdate=c2d,con_e=0,con_f=0,con_s=0)
    c2.save()
    c3=shipd(shipid=11,shname='MO-103',shorig='Miami',shdest='Osaka',shdate=c3d,con_e=0,con_f=0,con_s=0)
    c3.save()
    c4=shipd(shipid=12,shname='MO-104',shorig='Miami',shdest='Osaka',shdate=c4d,con_e=0,con_f=0,con_s=0)
    c4.save()

    d1d=datetime.date(2021,6,6)
    d2d=datetime.date(2021,6,12)
    d3d=datetime.date(2021,6,18)
    d4d=datetime.date(2021,6,24)
    d1=shipd(shipid=13,shname='CPM-101',shorig='Cape Town',shdest='Miami',shdate=d1d,con_e=0,con_f=0,con_s=0)
    d1.save()
    d2=shipd(shipid=14,shname='CPM-102',shorig='Cape Town',shdest='Miami',shdate=d2d,con_e=0,con_f=0,con_s=0)
    d2.save()
    d3=shipd(shipid=15,shname='CPM-103',shorig='Cape Town',shdest='Miami',shdate=d3d,con_e=0,con_f=0,con_s=0)
    d3.save()
    d4=shipd(shipid=16,shname='CPM-104',shorig='Cape Town',shdest='Miami',shdate=d4d,con_e=0,con_f=0,con_s=0)
    d4.save()

    e1d=datetime.date(2021,6,7)
    e2d=datetime.date(2021,6,13)
    e3d=datetime.date(2021,6,19)
    e4d=datetime.date(2021,6,25)
    e1=shipd(shipid=17,shname='CPCH-101',shorig='Cape Town',shdest='Chennai',shdate=e1d,con_e=0,con_f=0,con_s=0)
    e1.save()
    e2=shipd(shipid=18,shname='CPCH-102',shorig='Cape Town',shdest='Chennai',shdate=e2d,con_e=0,con_f=0,con_s=0)
    e2.save()
    e3=shipd(shipid=19,shname='CPCH-103',shorig='Cape Town',shdest='Chennai',shdate=e3d,con_e=0,con_f=0,con_s=0)
    e3.save()
    e4=shipd(shipid=20,shname='CPCH-104',shorig='Cape Town',shdest='Chennai',shdate=e4d,con_e=0,con_f=0,con_s=0)
    e4.save()

    f1d=datetime.date(2021,6,8)
    f2d=datetime.date(2021,6,14)
    f3d=datetime.date(2021,6,20)
    f4d=datetime.date(2021,6,26)
    f1=shipd(shipid=21,shname='CPO-101',shorig='Cape Town',shdest='Osaka',shdate=f1d,con_e=0,con_f=0,con_s=0)
    f1.save()
    f2=shipd(shipid=22,shname='CPO-102',shorig='Cape Town',shdest='Osaka',shdate=f2d,con_e=0,con_f=0,con_s=0)
    f2.save()
    f3=shipd(shipid=23,shname='CPO-103',shorig='Cape Town',shdest='Osaka',shdate=f3d,con_e=0,con_f=0,con_s=0)
    f3.save()
    f4=shipd(shipid=24,shname='CPO-104',shorig='Cape Town',shdest='Osaka',shdate=f4d,con_e=0,con_f=0,con_s=0)
    f4.save()

    g1d=datetime.date(2021,6,3)
    g2d=datetime.date(2021,6,9)
    g3d=datetime.date(2021,6,15)
    g4d=datetime.date(2021,6,21)
    g1=shipd(shipid=25,shname='CHM-101',shorig='Chennai',shdest='Miami',shdate=g1d,con_e=0,con_f=0,con_s=0)
    g1.save()
    g2=shipd(shipid=26,shname='CHM-102',shorig='Chennai',shdest='Miami',shdate=g2d,con_e=0,con_f=0,con_s=0)
    g2.save()
    g3=shipd(shipid=27,shname='CHM-103',shorig='Chennai',shdest='Miami',shdate=g3d,con_e=0,con_f=0,con_s=0)
    g3.save()
    g4=shipd(shipid=28,shname='CHM-104',shorig='Chennai',shdest='Miami',shdate=g4d,con_e=0,con_f=0,con_s=0)
    g4.save()

    h1d=datetime.date(2021,6,4)
    h2d=datetime.date(2021,6,10)
    h3d=datetime.date(2021,6,16)
    h4d=datetime.date(2021,6,22)
    h1=shipd(shipid=29,shname='CHCP-101',shorig='Chennai',shdest='Cape Town',shdate=h1d,con_e=0,con_f=0,con_s=0)
    h1.save()
    h2=shipd(shipid=30,shname='CHCP-102',shorig='Chennai',shdest='Cape Town',shdate=h2d,con_e=0,con_f=0,con_s=0)
    h2.save()
    h3=shipd(shipid=31,shname='CHCP-113',shorig='Chennai',shdest='Cape Town',shdate=h3d,con_e=0,con_f=0,con_s=0)
    h3.save()
    h4=shipd(shipid=32,shname='CHCP-104',shorig='Chennai',shdest='Cape Town',shdate=h4d,con_e=0,con_f=0,con_s=0)
    h4.save()

    i1d=datetime.date(2021,6,5)
    i2d=datetime.date(2021,6,11)
    i3d=datetime.date(2021,6,17)
    i4d=datetime.date(2021,6,23)
    i1=shipd(shipid=33,shname='CHO-101',shorig='Chennai',shdest='Osaka',shdate=i1d,con_e=0,con_f=0,con_s=0)
    i1.save()
    i2=shipd(shipid=34,shname='CHO-102',shorig='Chennai',shdest='Osaka',shdate=i2d,con_e=0,con_f=0,con_s=0)
    i2.save()
    i3=shipd(shipid=35,shname='CHO-103',shorig='Chennai',shdest='Osaka',shdate=i3d,con_e=0,con_f=0,con_s=0)
    i3.save()
    i4=shipd(shipid=36,shname='CHO-104',shorig='Chennai',shdest='Osaka',shdate=i4d,con_e=0,con_f=0,con_s=0)
    i4.save()

    j1d=datetime.date(2021,6,6)
    j2d=datetime.date(2021,6,12)
    j3d=datetime.date(2021,6,18)
    j4d=datetime.date(2021,6,24)
    j1=shipd(shipid=37,shname='OM-101',shorig='Osaka',shdest='Miami',shdate=j1d,con_e=0,con_f=0,con_s=0)
    j1.save()
    j2=shipd(shipid=38,shname='OM-102',shorig='Osaka',shdest='Miami',shdate=j2d,con_e=0,con_f=0,con_s=0)
    j2.save()
    j3=shipd(shipid=39,shname='OM-103',shorig='Osaka',shdest='Miami',shdate=j3d,con_e=0,con_f=0,con_s=0)
    j3.save()
    j4=shipd(shipid=40,shname='OM-104',shorig='Osaka',shdest='Miami',shdate=j4d,con_e=0,con_f=0,con_s=0)
    j4.save()

    k1d=datetime.date(2021,6,7)
    k2d=datetime.date(2021,6,13)
    k3d=datetime.date(2021,6,19)
    k4d=datetime.date(2021,6,25)
    k1=shipd(shipid=41,shname='OCP-101',shorig='Osaka',shdest='Cape Town',shdate=k1d,con_e=0,con_f=0,con_s=0)
    k1.save()
    k2=shipd(shipid=42,shname='OCP-102',shorig='Osaka',shdest='Cape Town',shdate=k2d,con_e=0,con_f=0,con_s=0)
    k2.save()
    k3=shipd(shipid=43,shname='OCP-103',shorig='Osaka',shdest='Cape Town',shdate=k3d,con_e=0,con_f=0,con_s=0)
    k3.save()
    k4=shipd(shipid=44,shname='OCP-104',shorig='Osaka',shdest='Cape Town',shdate=k4d,con_e=0,con_f=0,con_s=0)
    k4.save()

    l1d=datetime.date(2021,6,8)
    l2d=datetime.date(2021,6,14)
    l3d=datetime.date(2021,6,20)
    l4d=datetime.date(2021,6,26)
    l1=shipd(shipid=45,shname='OCH-101',shorig='Osaka',shdest='Chennai',shdate=l1d,con_e=0,con_f=0,con_s=0)
    l1.save()
    l2=shipd(shipid=46,shname='OCH-102',shorig='Osaka',shdest='Chennai',shdate=l2d,con_e=0,con_f=0,con_s=0)
    l2.save()
    l3=shipd(shipid=47,shname='OCH-103',shorig='Osaka',shdest='Chennai',shdate=l3d,con_e=0,con_f=0,con_s=0)
    l3.save()
    l4=shipd(shipid=48,shname='OCH-104',shorig='Osaka',shdest='Chennai',shdate=l4d,con_e=0,con_f=0,con_s=0)
    l4.save()
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
    lastnum=orderss.objects.last()
    lid=lastnum.id
    lid+=1
    return render(request, 'blogs/home.html', {'contexts':contexts,'contextss':contextss,'num':range(1,lid)})


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
        con=orderss.objects.last()
        h=str(con.date)
        h=h.split('-')
        h2=int(h[2]) #dayofmonth
        h3=int(h[1]) #Month num
        h4=int(h[0]) #Year
        h5=((int(h[1])-1)//3)+1 #Quarter
        h6=(int(datetime.date(int(h[0]),int(h[1]),int(h[2])).strftime("%W"))) #Weekofyear   
        h7=(datetime.datetime.strptime(str(con.date), '%Y-%m-%d').weekday()+1) #Dayofweek
        h8=(datetime.datetime.strptime(str(con.date),'%Y-%m-%d').timetuple().tm_yday) #Dayofyear
        a=con.id
        yy=analytics.objects.last()
        y=analytics(
            id=yy.id+1,
            OrderID=yy.id+1,
            Odate=con.date,
            DayofMonth=h2,
            Month=h3,
            Year=h4,
            Quarter=h5,
            DayofWeek=h7,
            DayofYear=h8,
            WeekofYear=h6,
            Sender = sen_n,
            Senderphone = sen_p,
            Receiver = rec_n,
            Receiverphone = rec_p,
            Origin = org,
            Destination = d,
            Typeofgoods = tg,
            Weight=w,   
            Priority = p,
            Rej=ro,
            NoofShipDays=shipsd,
            Cost=c,
            ShipID=sid
        )
        y.save()

        return redirect('blogs-register-2')
        return render(request, 'blogs/register-2.html')
    else:
        return render(request, 'blogs/register.html',{'contexts':contexts,'contextss':contextss})

def dashboard(request):
# For paasing the weight of goods in chartJS
    l={'con_e':0,'con_f':0,'con_s':0}
    for i in shipd.objects.all():
        l['con_e']+=i.con_e
        l['con_f']+=i.con_f
        l['con_s']+=i.con_s

    ces=l['con_e']
    cfs=l['con_f']
    css=l['con_s']
    print(l)
#for passing weight in each ship
    cs=0
    lm=[]
    for j in range(1,49):
        sb= shipd.objects.get(shipid=j)
        cs= sb.con_e+sb.con_f+sb.con_s
        lm.append(cs)
    aa=lm[0]
    bb=lm[1]
    cc=lm[2]
    dd=lm[3]
    ee=lm[4]
    ff=lm[5]
    gg=lm[6]
    hh=lm[7]
    ii=lm[8]
    jj=lm[9]
    kk=lm[10]
    ll=lm[11]
    print(lm)
# For passing the type of good in ChartJS
    s={'Eatables':0,'Solids':0,'Fluids':0}
    for i in orderss.objects.all():
        if i.rej==0:
            s[i.t_g]+=1

    b=s['Eatables']
    c=s['Solids']
    e=s['Fluids']
    print(s)

#Approved Orders Card
    t={'zero':0,'one':0}
    for i in orderss.objects.all():
        if i.rej==0:
            t['zero']+=1
        else:
            t['one']+=1

    a=t['zero']
    r=t['one']

#Busiest Ports Card
    d={'Miami':0,'Chennai':0, 'Cape Town':0,'Osaka':0}
    for i in orderss.objects.all():
        if i.rej==0:
            d[i.orgin]+=1
            d[i.dest]+=1
    Keymax = max(d, key=d.get)

#Latest Routes
    lo=""
    ld=""
    for i in orderss.objects.all():
        if(i.rej==0):
            lo=i.orgin
            ld=i.dest

#total Revenue
    ct=0
    for i in orderss.objects.all():
        if(i.rej==0):
            ct+=i.cost

#Urgent Orders
    cu=0
    for i in orderss.objects.all():
        if(i.rej==0 and i.pri=="Urgent"):
            cu+=1


        


    labels = []
    data = []
    for i in orderss.objects.all():
        city=orderss.objects.get(id=i.id)
        labels.append(str(city.date))
    
    labels=set(labels)
    labels=list(labels)
    labels.sort()
    val=0
    
    for i in range(len(labels)):
        for j in orderss.objects.all():
            dstr=str(j.date)
            if(labels[i]==dstr):
                val+=j.cost
        data.insert(i,val)
        val=0

    print(labels)
    print(data)

    return render(request, 'blogs/dashboard.html', {'to':a,'bur':Keymax,'r':r,'b':b,'c':c,'e':e,'ces':ces,'cfs':cfs,'css':css,'aa':aa,'bb':bb,'cc':cc,'dd':dd,'ee':ff,'gg':gg,'hh':hh,'ii':ii,'jj':jj,'kk':kk,'ll':ll,'lo':lo,'ld':ld,'ct':ct,'cu':cu,'labels':labels,'data':data})



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