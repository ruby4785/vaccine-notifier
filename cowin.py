import requests 
import time 
import json
import math
import random
from fake_useragent import UserAgent

class Data:
    def __init__(self):
        self.availability = self.get_availability()
        #print("Bot Started")
        #requests.post("https://api.telegram.org/bot1872421161:AAEByLFIqqWo-ygzGOqRBiuCyHsaNqnyytg/sendMessage?chat_id=-510229946&text=<b>18+Bot Started at: </b>"+time.asctime( time.localtime(time.time()) )+"&parse_mode=html")
        #requests.post("https://api.telegram.org/bot1790860894:AAEiylHiz1DN2-dMIjbVmIa8PE-6RFcmyak/sendMessage?chat_id=-510229946&text=<b>45+Bot Started at </b>"+time.asctime( time.localtime(time.time()) )+"&parse_mode=html")
    def get_date(self):
        date = time.strftime('%d-%m-%Y', time.localtime())
        return date
    def get_data(self):
        date=self.get_date()
        #temp_user_agent = UserAgent()
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    "origin": "https://selfregistration.cowin.gov.in",
                    "referer": "https://selfregistration.cowin.gov.in/",
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'no-cache',
                    'dnt': '1',
                    'pragma': 'no-cache',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
                             
        url1="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date="+date
        url2="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=265&date="+date
        #url3="https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=276&date="+date
        response1 = requests.get(url1,headers=headers)
        response2 = requests.get(url2,headers=headers)
        #response3 = requests.get(url3,headers=headers)
        dict1 = json.loads(response1.text)   
        dict2 = json.loads(response2.text)
        # dict3 = json.loads(response3.text)
        for values in range(len(dict2['centers'])):
       	    dict1['centers'].append(dict2['centers'][values])
        #for values in range(len(dict3['centers'])):
        #dict1['centers'].append(dict3['centers'][values])    
        return dict1
    def get_availability(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        data = self.get_data()
        dict={}
        for center in range(len(data["centers"])):
            for session in range(len(data['centers'][center]['sessions'])):
                if data['centers'][center]['sessions'][session]['available_capacity']>5:
                    center_name = data['centers'][center]['name']
                    center_district=data['centers'][center]['district_name']
                    center_address = data['centers'][center]['address']
                    center_pincode = data['centers'][center]['pincode']
                    center_vaccine = data['centers'][center]['sessions'][session]['vaccine']
                    center_availability = data['centers'][center]['sessions'][session]['available_capacity']
                    center_age = data['centers'][center]['sessions'][session]['min_age_limit']
                    avail_date = data['centers'][center]['sessions'][session]['date']
                    session_id =data['centers'][center]['sessions'][session]['session_id']
                    dose_1 = data['centers'][center]['sessions'][session]["available_capacity_dose1"]
                    dose_2 = data['centers'][center]['sessions'][session]["available_capacity_dose2"]
                    dict[session_id]=[center_name,center_address,center_pincode,center_district,center_vaccine,center_availability,center_age,avail_date,session_id,dose_1,dose_2]
        self.availability = dict
        return dict  
    def poll(self):
        old_availability = self.availability
        new_availability = self.get_availability()
        availability = new_availability.keys() - old_availability.keys()
        if len(availability)!=0:
            print("NEW Availability :\n")
            self.send_notification(availability)
        time.sleep(6.2)    
        return 
    def send_notification(self,availability):
        data = self.availability
        s=""
        a=""
        for session_id in availability:
            if data[session_id][6]==18:
                s+="🏥: "+str(data[session_id][0])
                s+="\n"
                s+="📌: "+str(data[session_id][1])
                s+="\n"
                s+="Pincode: ["+str(data[session_id][2])+"]"
                s+="\n"
                s+="District: "+str(data[session_id][3])
                s+="\n"
                s+="Vaccine: "+str(data[session_id][4])
                s+="\n"
                s+="Age Group: "+str(data[session_id][6])+"+" 
                s+="\n"
                s+="Availability :"
                s+="\n"
                s+="   Dose 1 💉: "+str(data[session_id][9])
                s+="\n"
                s+="   Dose 2 💉: "+str(data[session_id][10])
                s+="\n"
                s+="Date 📅: "+str(data[session_id][7])
                s+="\n"
                s+="session_id: "+str(data[session_id][8])
                s+="\n"
                s+="\n"
                s+="⚠**Use Aarogya Setu App to avoid captcha.**"
                s+="\n"
                s+="\n"
                s+="🔗Cowin : https://selfregistration.cowin.gov.in/"
                s+="\n"
                s+="-----------------------------------------"
                s+="\n"
            else:
                a+="🏥: "+str(data[session_id][0])
                a+="\n"
                a+="📌: "+str(data[session_id][1])
                a+="\n"
                a+="Pincode: ["+str(data[session_id][2])+"]"
                a+="\n"
                a+="District: "+str(data[session_id][3])
                a+="\n"
                a+="Vaccine: "+str(data[session_id][4])
                a+="\n"
                a+="Age Group: "+str(data[session_id][6])+"+" 
                a+="\n"
                a+="Availability :"
                a+="\n"
                a+="   Dose 1 💉: "+str(data[session_id][9])
                a+="\n"
                a+="   Dose 2 💉: "+str(data[session_id][10])
                a+="\n"
                a+="Date 📅: "+str(data[session_id][7])
                a+="\n"
                a+="session_id: "+str(data[session_id][8])
                a+="\n"
                a+="\n"
                a+="⚠**Use Aarogya Setu App to avoid captcha.**"
                a+="\n"
                a+="\n"
                a+="🔗Cowin : https://selfregistration.cowin.gov.in/"
                a+="\n"
                a+="-----------------------------------------"
                a+="\n"
        print(a)
        print(s)
        print(len(a))
        print(len(s))        
        if s!="":
            num_of_times=int(math.ceil(len(s)/4096))
            k=4095
            i=0
            for _ in range(num_of_times):
                requests.post("https://api.telegram.org/bot1872421161:AAEByLFIqqWo-ygzGOqRBiuCyHsaNqnyytg/sendMessage?chat_id=-1001230703890&text="+s[i:k])
                i=k
                k+=4095
        if a!="":
            num_of_times=int(math.ceil(len(a)/4096))
            k=4095
            i=0
            for _ in range(num_of_times):
                requests.post("https://api.telegram.org/bot1790860894:AAEiylHiz1DN2-dMIjbVmIa8PE-6RFcmyak/sendMessage?chat_id=-1001162225447&text="+a[i:k])
                i=k
                k+=4095
        return
def main():
    data = Data()
    while True:
        data.poll()
while(1):
    try:
        main()
    except Exception as e:
        print(e)
        time.sleep(5)



