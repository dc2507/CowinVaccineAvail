from pushbullet import PushBullet
import http.client
from datetime import date, datetime
import json

# figuring out date in specified format
today = date.today()
d1 = today.strftime("%d-%m-%Y")

# making GET request
conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
payload = ''
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
query = "/api/v2/appointment/sessions/public/findByDistrict?district_id=505&date="+str(d1)
conn.request("GET", query, payload, headers)
res = conn.getresponse()
data = res.read()
dataUTF = data.decode("utf-8")
dataDICT = json.loads(dataUTF)

# counting number of centers
count=0
for x in dataDICT:
    if(isinstance(dataDICT[x], list)):
        count += len(dataDICT[x])
now = (datetime.now()).strftime("%H:%M:%S")
ininfo1 = f"Vaccination Slot Info JPR1 - {d1} {now}"
info1 = ""
# printing centres information
for i in range(0,count):
    dose1 = dataDICT["sessions"][i]['available_capacity_dose1']
    min_age = int(dataDICT["sessions"][i]['min_age_limit'])
    if min_age==18 & dose1>0:
        info1 += f"""
                ************************
                Center Name : {dataDICT["sessions"][i]['name']}
                Min Age Limit : {dataDICT["sessions"][i]['min_age_limit']}
                Vaccine : {dataDICT["sessions"][i]['vaccine']}
                Available Capacity Dose 1 : {dataDICT["sessions"][i]['available_capacity_dose1']} 
                Available Capacity Dose 2 : {dataDICT["sessions"][i]['available_capacity_dose1']}
                Fee : {dataDICT["sessions"][i]['fee_type']}
                Pincode : {dataDICT["sessions"][i]['pincode']}
                ************************"""

# publish notification
API_KEY = "YOUR_API_KEY"
pb = PushBullet(API_KEY)
push = pb.push_note(ininfo1, info1)
