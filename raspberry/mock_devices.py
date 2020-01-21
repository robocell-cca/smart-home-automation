from requests import get
import time



led={7,11,13}
while True:
    
    r =get('http://192.168.31.7:8000/manage/api/devices/')
    count=0
    for d in r.json():
        #print(d)
        if d["state"] == '0':
    ##        ledoff(led[count])
            print("led",count,"off")
        else:
    ##        ledon(led[count])
            print("led",count,"on")
        count+=1
    print("")
    time.sleep(3)
