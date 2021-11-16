from os import access
import cv2 
import dropbox
import time
import random

starttime = time.time()
def takeSnapShot():
    number = random.randint(0,100)
     #initializing cv2 
    videoCaptureObject = cv2.VideoCapture(0) 
    result = True
    while(result):
        #read the frames while the camera is on 
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device 
        img_name = "img"+str(number)+".png" 
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name 
    print("snapshot taken") 
    # releases the camera 
    videoCaptureObject.release()
    # closes all the window that might be opened while this process 
    cv2.destroyAllWindows()

takeSnapShot()

def upload_file(image_name):
access_token ='sl.A8BpHQV9m2d4W6qCnFVZedtWHEUgNQM4SLVm4p358ZdTv2gVn5Q3V9c8vVvtfhlp5cQqkWIUObVQ0RwHH7rzdMmec4W6uuGBbDIy31sy95Es3O5t2UvSmY_JLB1UJJpPi5zUUk0'
file= image_name
file_form = file
file_to = "/newFolder1" + (image_name)
dbx = dropbox.Dropbox(access_token)

with open(file_form,'rb') as f:
    dbx.files_upload(f.read(),file_to,mode = dropbox.files.writeMode.overWrite)
    print("file uploaded")

def main():
    while(True): 
        if ((time.time() - starttime) >= 4):
             name = takeSnapShot()
             upload_file(name)
               
main()
