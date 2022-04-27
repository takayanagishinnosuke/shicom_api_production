import cv2
import numpy as np
import os 
from time import sleep


key = 'OK'

 # カメラのポート番号指定
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

##--推論モデルの定義--##
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

##--ただのフォント指定--##
font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'mam', 'Paula', 'Ilza', 'Z', 'W'] 


# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)


# while True: ##--カメラを常時起動する場合のwhile文--#
ret, img =cam.read()

##--ラズパイ用の反転コード--##
# img = cv2.flip(img, -1) # Flip vertically

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale( 
    gray,
    scaleFactor = 1.2,
    minNeighbors = 5,
    minSize = (int(minW), int(minH)),
)

for(x,y,w,h) in faces:

    cv2.rectangle(gray, (x,y), (x+w,y+h), (0,255,0), 2)

    id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

    # Check if confidence is less them 100 ==> "0" is perfect match 
    if (confidence < 100):
        id = names[id]
        key = 'NG'
        confidence = "  {0}%".format(round(100 - confidence))
    else:
        id = "unknown"
        confidence = "  {0}%".format(round(100 - confidence))
    
    cv2.putText(gray, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
    cv2.putText(gray, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  

        
        
    ##--カメラ映像をディスプレイに表示(あっても無くても)--##
    #cv2.imshow('camera',gray) 



##---カメラ常時起動時の終了コマンド--
    # k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    # if k == 27: # Escでbreak
    #     break

    # target_time = 3
    # start_time = 0

##--カメラ常時起動時の終了タイマーコード--##

    # def up_timer(secs):
    #     for i in range(0,secs):
    #         sleep(1)
    #         global start_time
    #         start_time = start_time +i
        
            
    
    # up_timer(target_time)
    # if target_time <= start_time:
    #     print('おわりんこ')
    #     break
    


## --カメラ初期化--##
print("\n [INFO] Exiting Program and cleanup stuff")
print(key)
cam.release() ##cam.releseで終了
cv2.destroyAllWindows() ##メモリの解放


