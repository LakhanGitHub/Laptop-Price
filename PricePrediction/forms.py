from django import forms

# forms.py
from django import forms

import pickle
import os
from django.conf import settings
import pandas as pd

# Load the model once when the server starts
MODEL_PATH = os.path.join(settings.BASE_DIR, 'Computer_Data.pkl')

# Load the model
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)
df = pd.read_pickle(MODEL_PATH)

Compay = df.Company.unique()
Type = df.TypeName.unique()
CPU = df['Cpu brand'].unique()
GPU = df['Gpu brand'].unique()
OS = df.OS.unique()

#print(compay)

Screen_resolution = ['1440x900','1366x778','1600x900','1920x1080','2880x1800',
                   '2560x1600','3840x2160','3200x1800','2880x1800','2560x1440','2304x1440']
IPS = ['Yes','No']
touch = ['Yes','No']
RAM = [0,2,4,6,8,16,32,64,128]
HDD = [0,8,32,64,128,256,512,1024]
SSD = [0,8,32,64,128,256,512,1024]

class PredictionForm(forms.Form):
    Company = forms.ChoiceField(required=True,widget=forms.Select({'class':'form-control'}))
    TypeName = forms.ChoiceField(required=True,widget=forms.Select({'class':'form-control'}))
    RAM = forms.ChoiceField(required=True,label='RAM (In GB)',widget=forms.Select({'class':'form-control'}))
    Weight = forms.FloatField(required=True,label='Weight: (e.g-1.2kg)',widget=forms.NumberInput(attrs={'class':'form-control'}))
    TouchScreen = forms.ChoiceField(required=True,label='Touch Screen', widget=forms.Select({'class':'form-control'}))
    IPSDisplay = forms.ChoiceField(required=True,label='IPS Display', widget=forms.Select({'class':'form-control'}))
    screensize = forms.FloatField(required=True,label='Screen Size (e.g 15.6")',widget=forms.NumberInput(attrs={'class':'form-control'}))
    ScreenResolustion = forms.ChoiceField(required=True,label='Screen Resolustion',widget=forms.Select({'class':'form-control'}))
    CPU = forms.ChoiceField(required=True,label='CPU',widget=forms.Select({'class':'form-control'}))
    GPU = forms.ChoiceField(required=True,label='GPU',widget=forms.Select({'class':'form-control'}))
    OS = forms.ChoiceField(required=True,label='Operating System (OS)',widget=forms.Select({'class':'form-control'}))
    HDD = forms.ChoiceField(required=True,label='HDD (In GB)',widget=forms.Select({'class':'form-control'}))
    SSD = forms.ChoiceField(required=True,label='SDD (In GB)',widget=forms.Select({'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(PredictionForm, self).__init__(*args, **kwargs)
        # Fetch unique category values from the Product model
        #companies = df.Company.unique()
        choices_comp = [(category, category) for category in Compay]
        choices_comp.insert(0, ('', 'Select an option...'))
        self.fields['Company'].choices = choices_comp

        choice_type = [(category, category) for category in Type]
        choice_type.insert(0, ('', 'Select an option...'))
        self.fields['TypeName'].choices = choice_type

        choice_cpu = [(category, category) for category in CPU]
        choice_cpu.insert(0, ('', 'Select an option...'))
        self.fields['CPU'].choices = choice_cpu

        choice_gpu = [(category, category) for category in GPU]
        choice_gpu.insert(0, ('', 'Select an option...'))
        self.fields['GPU'].choices = choice_gpu

        choice_os = [(category, category) for category in OS]
        choice_os.insert(0, ('', 'Select an option...'))
        self.fields['OS'].choices = choice_os

        choice_touch = [(category, category) for category in touch]
        choice_touch.insert(0, ('', 'Select an option...'))
        self.fields['TouchScreen'].choices = choice_touch

        choice_resolution = [(category, category) for category in Screen_resolution]
        choice_resolution.insert(0, ('', 'Select an option...'))
        self.fields['ScreenResolustion'].choices = choice_resolution

        choice_ips = [(category, category) for category in IPS]
        choice_ips.insert(0, ('', 'Select an option...'))
        self.fields['IPSDisplay'].choices = choice_ips

        choice_ram = [(category, category) for category in RAM]
        choice_ram.insert(0, ('', 'Select an option...'))
        self.fields['RAM'].choices = choice_ram

        choice_hdd = [(category, category) for category in HDD]
        choice_hdd.insert(0, ('', 'Select an option...'))
        self.fields['HDD'].choices = choice_hdd

        choice_ssd = [(category, category) for category in SSD]
        choice_ssd.insert(0, ('', 'Select an option...'))
        self.fields['SSD'].choices = choice_ssd



