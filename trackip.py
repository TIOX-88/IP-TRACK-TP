import os
import urllib3
import json 

while True:
    os.system("clear")
    print(""" 
            
             ________                                       _______   __                       __                     
/        |                                     /       \ /  |                     /  |                    
$$$$$$$$/______    ______   _____  ____        $$$$$$$  |$$/   ______   ______   _$$ |_     ______        
   $$ | /      \  /      \ /     \/    \       $$ |__$$ |/  | /      \ /      \ / $$   |   /      \       
   $$ |/$$$$$$  | $$$$$$  |$$$$$$ $$$$  |      $$    $$/ $$ |/$$$$$$  |$$$$$$  |$$$$$$/   /$$$$$$  |      
   $$ |$$    $$ | /    $$ |$$ | $$ | $$ |      $$$$$$$/  $$ |$$ |  $$/ /    $$ |  $$ | __ $$    $$ |      
   $$ |$$$$$$$$/ /$$$$$$$ |$$ | $$ | $$ |      $$ |      $$ |$$ |     /$$$$$$$ |  $$ |/  |$$$$$$$$/       
   $$ |$$       |$$    $$ |$$ | $$ | $$ |      $$ |      $$ |$$ |     $$    $$ |  $$  $$/ $$       |      
   $$/  $$$$$$$/  $$$$$$$/ $$/  $$/  $$/       $$/       $$/ $$/       $$$$$$$/    $$$$/   $$$$$$$/                                                               
                                                                           
                                                                           
########################################################################
##   Developer : TIOX VAU                                             ##  
##   Github :https://github.com/TIOX-88                               ##
##   YouTub ;https://www.youtube.com/channel/UCo1_rtFpX9ILWblRhUX2bFQ ##
##   Facebook; https://www.facebook.com/tiox.VAUn                     ##
########################################################################
----------------------------------------------------
----------------------------------------------------
      """)
    ip=input("What is your target IP: ") 
    url = "http://ip-api.com/json/"
    response = urllib3.urlopen(url + ip)
    data = response.read() 
    values = json. loads (data)


    print(" IP: " + values['query'])
    print(" City: " + values['city'])
    print(" ISP: " + values['isp'])
    print ("Country: " + values['country'])
    print ("Region: " + values['region'])
    print("Time zone: " + values['timezone'])

    break