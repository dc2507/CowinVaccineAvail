# CowinVaccineAvail

This script provides a core function for finding out vaccine availability by district IDs. Made using the public Cowin APIs as mentioned on API Setu.


Usage:
------
python cowinScript.py <DISTRICT_ID_NUM>

For District ID list - 
----------------------
Simply visit browser to this public api link - 

For figuring out your state ID-
https://cdn-api.co-vin.in/api/v2/admin/location/states?Accept-Language=hi_IN

Further you can query the district by replacing state ID=29 with your state in below URL
https://cdn-api.co-vin.in/api/v2/admin/location/districts/29?Accept-Language=hi_IN

<br>
You can further extend this script to any functionality - I, for my ease have enabled mobile notifications using PUSHBULLET and scheduled them hourly to get a availability note so that we don't need to log on to our PCs and check often. You can schedule them at any frequency (up to you). 
