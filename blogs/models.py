from django.db import models

# Create your models here.





class shipd(models.Model):
    shipid=models.IntegerField()
    shname = models.CharField(max_length=100, null= True, blank=True)
    shorig = models.CharField(max_length=100, null= True, blank=True)
    shdest = models.CharField(max_length=100, null= True, blank=True)
    shdate = models.DateField()
    con_e=models.IntegerField()
    con_f=models.IntegerField()
    con_s=models.IntegerField()




class orderss(models.Model):
    sen_name = models.CharField(max_length=100, null= True, blank=True)
    sen_add = models.TextField()
    sen_ph = models.CharField(max_length=100, null= True, blank=True)
    rec_name = models.CharField(max_length=100, null= True, blank=True)
    rec_add = models.TextField()
    rec_ph = models.CharField(max_length=100, null= True, blank=True)
    t_g = models.CharField(max_length=100, null= True, blank=True)
    orgin = models.CharField(max_length=100,null= True, blank=True)
    dest = models.CharField(max_length=100,null= True, blank=True)
    pri = models.CharField(max_length=100,null= True, blank=True)
    nodays=models.IntegerField()
    weight=models.IntegerField()
    rej=models.IntegerField()
    cost=models.IntegerField()
    shipid=models.IntegerField()
    dd = models.CharField(max_length=100,null= True, blank=True)
    dm = models.CharField(max_length=100,null= True, blank=True)
    dy = models.CharField(max_length=100,null= True, blank=True)
    ddd = models.CharField(max_length=100,null= True, blank=True)
    date=models.DateField(auto_now=True)

class analytics(models.Model):
    OrderID=models.IntegerField()
    Odate=models.DateField()
    DayofMonth=models.IntegerField()
    Month=models.IntegerField()
    Year=models.IntegerField()
    Quarter=models.IntegerField()
    DayofWeek=models.IntegerField()
    DayofYear=models.IntegerField()
    WeekofYear=models.IntegerField()
    Sender = models.CharField(max_length=100, null= True, blank=True)
    Senderphone = models.CharField(max_length=100, null= True, blank=True)
    Receiver = models.CharField(max_length=100, null= True, blank=True)
    Receiverphone = models.CharField(max_length=100, null= True, blank=True)
    Origin = models.CharField(max_length=100,null= True, blank=True)
    Destination = models.CharField(max_length=100,null= True, blank=True)
    Typeofgoods = models.CharField(max_length=100, null= True, blank=True)
    Weight=models.IntegerField()   
    Priority = models.CharField(max_length=100,null= True, blank=True)
    Rej=models.IntegerField()
    NoofShipDays=models.IntegerField()
    Cost=models.IntegerField()
    ShipID=models.IntegerField()












'''

class Des(models.Model):
    sen_name = models.CharField(max_length=100, null= True, blank=True)
    sen_add = models.TextField()
    sen_ph = models.CharField(max_length=100, null= True, blank=True)
    rec_name = models.CharField(max_length=100, null= True, blank=True)
    rec_add = models.TextField()
    rec_ph = models.CharField(max_length=100, null= True, blank=True)
    t_g = models.CharField(max_length=100, null= True, blank=True)
    orgin = models.CharField(max_length=100,null= True, blank=True)
    dest = models.CharField(max_length=100,null= True, blank=True)
    pri = models.CharField(max_length=100,null= True, blank=True)
    shipment=models.IntegerField()


    {% extends "blogs/base.html" %}
{% block content %}
<script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>
<style>
  .widget-49 .widget-49-title-wrapper {
    display: flex;
    align-items: center;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-primary {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background-color: #edf1fc;
    width: 4rem;
    height: 4rem;
    border-radius: 50%;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-primary .widget-49-date-day {
    color: #4e73e5;
    font-weight: 500;
    font-size: 1.5rem;
    line-height: 1;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-primary .widget-49-date-month {
    color: #4e73e5;
    line-height: 1;
    font-size: 1rem;
    text-transform: uppercase;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-secondary {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background-color: #fcfcfd;
    width: 4rem;
    height: 4rem;
    border-radius: 50%;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-secondary .widget-49-date-day {
    color: #dde1e9;
    font-weight: 500;
    font-size: 1.5rem;
    line-height: 1;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-secondary .widget-49-date-month {
    color: #dde1e9;
    line-height: 1;
    font-size: 1rem;
    text-transform: uppercase;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-success {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background-color: #e8faf8;
    width: 4rem;
    height: 4rem;
    border-radius: 50%;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-success .widget-49-date-day {
    color: #17d1bd;
    font-weight: 500;
    font-size: 1.5rem;
    line-height: 1;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-success .widget-49-date-month {
    color: #17d1bd;
    line-height: 1;
    font-size: 1rem;
    text-transform: uppercase;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-info {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background-color: #ebf7ff;
    width: 4rem;
    height: 4rem;
    border-radius: 50%;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-info .widget-49-date-day {
    color: #36afff;
    font-weight: 500;
    font-size: 1.5rem;
    line-height: 1;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-info .widget-49-date-month {
    color: #01060a;
    line-height: 1;
    font-size: 1rem;
    text-transform: uppercase;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-warning {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background-color: #050505;
    width: 4rem;
    height: 4rem;
    border-radius: 50%;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-warning .widget-49-date-day {
    color: #fffefe;
    font-weight: 500;
    font-size: 1.5rem;
    line-height: 1;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-warning .widget-49-date-month {
    color: #fefeff;
    line-height: 1;
    font-size: 1rem;
    text-transform: uppercase;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-danger {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background-color: #feeeef;
    width: 4rem;
    height: 4rem;
    border-radius: 50%;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-danger .widget-49-date-day {
    color: #F95062;
    font-weight: 500;
    font-size: 1.5rem;
    line-height: 1;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-danger .widget-49-date-month {
    color: #F95062;
    line-height: 1;
    font-size: 1rem;
    text-transform: uppercase;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-light {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background-color: #fefeff;
    width: 4rem;
    height: 4rem;
    border-radius: 50%;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-light .widget-49-date-day {
    color: #f7f9fa;
    font-weight: 500;
    font-size: 1.5rem;
    line-height: 1;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-light .widget-49-date-month {
    color: #f7f9fa;
    line-height: 1;
    font-size: 1rem;
    text-transform: uppercase;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-dark {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background-color: #ebedee;
    width: 4rem;
    height: 4rem;
    border-radius: 50%;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-dark .widget-49-date-day {
    color: #394856;
    font-weight: 500;
    font-size: 1.5rem;
    line-height: 1;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-dark .widget-49-date-month {
    color: #394856;
    line-height: 1;
    font-size: 1rem;
    text-transform: uppercase;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-base {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background-color: #f0fafb;
    width: 4rem;
    height: 4rem;
    border-radius: 50%;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-base .widget-49-date-day {
    color: #68CBD7;
    font-weight: 500;
    font-size: 1.5rem;
    line-height: 1;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-date-base .widget-49-date-month {
    color: #68CBD7;
    line-height: 1;
    font-size: 1rem;
    text-transform: uppercase;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-meeting-info {
    display: flex;
    flex-direction: column;
    margin-left: 1rem;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-meeting-info .widget-49-pro-title {
    color: #3c4142;
    font-size: 14px;
  }
  
  .widget-49 .widget-49-title-wrapper .widget-49-meeting-info .widget-49-meeting-time {
    color: #B1BAC5;
    font-size: 13px;
  }
  
  .widget-49 .widget-49-meeting-points {
    font-weight: 400;
    font-size: 13px;
    margin-top: .5rem;
  }
  
  .widget-49 .widget-49-meeting-points .widget-49-meeting-item {
    display: list-item;
    color: #727686;
  }
  
  .widget-49 .widget-49-meeting-points .widget-49-meeting-item span {
    margin-left: .5rem;
  }
  
  .widget-49 .widget-49-meeting-action {
    text-align: right;
  }
  
  .widget-49 .widget-49-meeting-action a {
    text-transform: uppercase;
  }


</style>
<div class="col-md-8">
  
  {%if des %}
    {% for dess in des %}

      {% if dess.rej == 0 %}
        <article class="media content-section bg-Secondary" style="background: linear-gradient(135deg, #23bdb8 0%, #43e794 100%) !important;">
      {% else %}
      <article class="media content-section bg-Secondary" style="background: linear-gradient(to right, #ff5050 0%, #ff9999 100%);">
      {% endif  %}
          <div class="media-body ">
            <!--div class="article-metadata"-->
              <h3>{{ dess.sen_name }} -> {{ dess.rec_name }}</h3>
              {%if dess.dest == "Mumbai" %}
              <small class="text-muted" style="color: blue;">{{ dess.orgin }} -> {{ dess.dest }}</small>
              {%else%}
              <small class="text-muted" style="color:black;">{{ dess.orgin }} -> {{ dess.dest }}</small>
              {% endif %}
            <!--/div-->
            <h2>Priority: {{ dess.pri }} <small>{{ dess.t_g }}</small> <right> &emsp;&emsp;&emsp; Rs.{{ dess.cost }} for <small><b>{{dess.weight}}Kgs</b></small></right></h2>
            <p class="article-content"> <br>This shipment will arrive in {{ dess.shipment }} days</p>
          </div>
        </article>

    {% endfor %}

    
    
  {% endif %} 



</div>


{% endblock content %}

'''
