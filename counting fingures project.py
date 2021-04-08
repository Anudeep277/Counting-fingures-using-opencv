#!/usr/bin/env python
# coding: utf-8

# In[17]:


import cv2
import time
import os
import  Handtrackingmodel as ht

wCam,hCam = 1080,720
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

ptime=0
detector=ht.handDetector(detectionCon=0.70)
trackids=[4,8,12,16,20]
while True:
    success,img=cap.read()
    image=detector.findHands(img)
    mylist=detector.findPosition(img,draw=False)
    #print(mylist)
    
    if len(mylist)!=0:  
        fingers=[]
        if mylist[trackids[0]][1] > mylist[trackids[0]-1][1]:
                 fingers.append(1)
        else:
                 fingers.append(0)
        for ids in range(1,5):
            if mylist[trackids[ids]][2] < mylist[trackids[ids]-2][2]:
                 fingers.append(1)
            else:
                 fingers.append(0)
            
            #print(fingers)
        totalfingers=fingers.count(1)
        #print(totalfingers)
        cv2.putText(img,f"{int(totalfingers)}",(50,600),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),40)
        
    ctime=time.time()
    FPS=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,f"FPS: {int(FPS)}",(50,120),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),3)
    cv2.imshow("image",img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




