 import cv2
import pickle
import numpy as np
import os # to store it in pickle file
video=cv2.VideoCapture(0) # opens the built in web camera and video is a camera object , opens inbuilt for 0 , external use 1
facedetect=cv2.CascadeClassifier('Data/haarcascade_frontalface_default.xml') # detects face using this file
faces_data=[]# empty list to store face data
name = input("Enter your name ")
i=0 
while True:
    ret,frame=video.read()# returns two values - if webcam is working or not and the other is the frames
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #To convert bgr images to grayscale
    faces=facedetect.detectMultiScale(gray, 1.3 ,5) # to get the coordinate values x , y ,w and h
    for (x,y,w,h) in faces :
        crop_img=frame[y:y+h, x:x+w, :]#to crop the required image
        resized_img = cv2.resize(crop_img,(50,50))
        if len(faces_data)<=100 and i%10==0 :
            faces_data.append(resized_img)
        i=i+1
        cv2.putText(frame,str(len(faces_data)),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)#To display the text on the image
                #            sixe of the frame , color and thickness
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),1)
    cv2.imshow("Frame",frame)#open a new window and show your face
    k=cv2.waitKey(1) # this will break the loop here when we click the q
    if k==ord('q') or len(faces_data)==100:
        break
video.release()#stop the webcam  
cv2.destroyAllWindows()#terminate all the windows
faces_data=np.asarray(faces_data)#converting into numpy array
faces_data=faces_data.reshape(100,-1) # we are reshaping so that this can be pased to machine learning model


if 'names.pkl' not in os.listdir('data/'):#create a names directory to store the names of the user
    names=[name]*100
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f) # saving it in pickle file
 else:
  # if it exist and creating another  user
  # concatinating here 
    with open('data/names.pkl', 'rb') as f:
        names=pickle.load(f)
    names=names+[name]*100
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)
# the same is being done for faces
# creating a new face intially
if 'faces_data.pkl' not in os.listdir('data/'):
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open('data/faces_data.pkl', 'rb') as f:
        faces=pickle.load(f)
    faces=np.append(faces, faces_data, axis=0) # adding the next user's face 
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces, f)
