import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os
from joblib import load

#page setup and title
st.set_page_config(page_title='Laptop-price👨‍💻',layout='wide')
st.header('Laptop Price predictor tool', divider="rainbow")

#load model data
#pipe = pickle.load(open('Pipe.pkl','rb')) #os.path.join('Computer_Pipe.pkl')
pipe = load('Pipe.pkl')
data_path = os.path.join('df.pkl')

#df_ =df.groupby('Company')['Price'].sum()
#st.bar_chart(df_)
#set progress status
#with st.spinner('Updating data...'):
df = pd.read_pickle(data_path)

c1,c2,c3 = st.columns(3)
with c1:
    compnamy = c1.selectbox('Company',df['Company'].unique())
    type = c1.selectbox('Type',df['TypeName'].unique())
    ram = c1.selectbox('RAM Size',np.sort(df['Ram'].unique()))
    weight = c1.number_input('Weight')
    toughscreen = c1.selectbox('Touch Screen',['yes','No'])

    if toughscreen =="Yes":
        toughscreen = 1
    else:
        toughscreen = 0

    ips = c1.selectbox('IPS',['Yes','No'])
    if ips =="Yes":
        ips = 1
    else:
        ips = 0

    screensize = c1.number_input('Screen Size')

    if screensize==0:
        screensize =0.1
    else:
        screensize

with c2:
    resolution = c2.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160'
                                               '3200x1800','2880x1800','2560x1600','2560x1440',
                                               '2304x1440'])
    cpu = c2.selectbox('CPU',df['Cpu brand'].unique())
    gpu = c2.selectbox('GPU',df['Gpu brand'].unique())
    os = c2.selectbox('OS',df['OS'].unique())
    hdd = c2.selectbox('HDD',[0,128,256,512,1040,2048])
    ssd = c2.selectbox('SSD',[0,8,128,256,512,1024])

    

#st.image('laptop.png','Create, Make and build something wounderfull!')
res_x = resolution.split('x')[0]
res_y = resolution.split('x')[1]
ppi = (((int(res_x))**2 + (int(res_y))**2)**.5)/float(screensize)

if c2.button('Predict Price'):
    #pass
    query = np.array([compnamy,type,ram,weight,toughscreen,ips,ppi,cpu,gpu,os,hdd,ssd])
    query = query.reshape(1,12)
    prediction ="The predicted price of this configuration is: Rs " + str(np.round(np.exp(pipe.predict(query)[0]),0))
    c3.subheader(prediction)


    
