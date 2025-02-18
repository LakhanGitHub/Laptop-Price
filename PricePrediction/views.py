from django.shortcuts import render
from .forms import PredictionForm
from django.http import HttpResponse, HttpResponseRedirect

import pickle
import os
from django.conf import settings
import pandas as pd
import numpy as np
import joblib

# Load the model once when the server starts
MODEL_PATH = os.path.join(settings.BASE_DIR, 'Computer_Data.pkl')
#pipe_path = os.path.join(settings.BASE_DIR, 'Computer_Pipe.pkl')

pipe_path = os.path.join(settings.BASE_DIR, 'Computer_Pipe.pkl')

# Load the model

#pipe = joblib.load(pipe_path)

df = pd.read_pickle(MODEL_PATH)

pipe = pd.read_pickle(pipe_path)

#comp_part = df.Company.unique()
#compay = tuple(df.Company.unique())


#print(df.head(2))
# Create your views here.

def predict(request):
    form = PredictionForm(request.POST or None)
    if request.method =='POST'and form.is_valid():
        #if form.is_valid:
            #process the selected catogery
        compnamy = form.cleaned_data['Company']
        type = form.cleaned_data['TypeName']
        ram = form.cleaned_data['RAM']
        weight = form.cleaned_data['Weight']
        touchscreen = form.cleaned_data['TouchScreen']
        if touchscreen =="Yes":
            touchscreen = 1
        else:
            touchscreen = 0

        ips = form.cleaned_data['IPSDisplay']
        if ips =="Yes":
            ips = 1
        else:
            ips = 0

        screensize = form.cleaned_data['screensize'] 
        if screensize==0:
            screensize =0.1
        else:
            screensize
        resolution = form.cleaned_data['ScreenResolustion']            
        cpu = form.cleaned_data['CPU']
        gpu = form.cleaned_data['GPU']
        os = form.cleaned_data['OS']
        hdd = form.cleaned_data['HDD']
        ssd = form.cleaned_data['SSD']
        res_x = resolution.split('x')[0]
        res_y = resolution.split('x')[1]
        ppi = (((int(res_x))**2 + (int(res_y))**2)**.5)/float(screensize)
        query = np.array([compnamy,type,ram,weight,touchscreen,ips,ppi,cpu,gpu,os,hdd,ssd])

        query = query.reshape(1,12)
        
        prediction ="The predicted price of this configuration is: Rs " + str(np.round(np.exp(pipe.predict(query)[0]),0))
        return render(request, 'priceprediction/home.html', {'form':form,'result':prediction})

    else:
        form = PredictionForm()
    return render(request, 'priceprediction/home.html', {'form':form})
