import cv2
import numpy as np
import os
import telcoll


def recognition(post):
  recognizer = cv2.face.LBPHFaceRecognizer_create()
  recognizer.read("trainer_custom.yml")
  cascadePath = "haarcascade_frontalface_default.xml"
  faceCascade = cv2.CascadeClassifier(cascadePath);

  names = ['None', 'mama', 'papa', 'ikeda'] 
  id =''
  key = ''
  confidence = None
  result = None

  # cap = cv2.VideoCapture(0)
  # cap.set(3,640)
  # cap.set(4,480)

    # img = cv2.imread('') #テスト用
    # im = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #テスト用

  im = post
  print(im)

  #---ビデオ確認用---##
# while True:
#   ret, ims = cap.read()
#   im = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)

#   cv2.imshow('video', im)

  """人かそうでないか"""
  hog = cv2.HOGDescriptor() ##特徴量抽出
  hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) #SVMで分類

  human = hog.detectMultiScale(im) #human検出


  for x in human:
    result = len(x) #resultの配列の数を格納

  """ママかパパか"""
  faces = faceCascade.detectMultiScale( 
        im,
        scaleFactor = 1.11,
        minNeighbors = 5,
        minSize=(50,50)
  )

  for(x,y,w,h) in faces:
    # cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 2)
    id, confidence = recognizer.predict(im[y:y+h,x:x+w])
    idname = names[id]
    confidence = max(0,round(100 - confidence))

  """最終判断"""
  if(result >=1 or len(faces) > 0):
    key = 'Danger'
    if(id == 'mama' or id == 'ikeda') and confidence >= 20:
      key = 'Super_Danger'
      telcoll.coll()

  elif(id == 'mama' or id == 'ikeda') and confidence >= 20:
    key = 'Super_Danger'
    telcoll.coll()

  else:
    key = 'Noproblem'

  print(key)

##--カメラ起動終了--##
#   keycomand = cv2.waitKey(1) & 0xFF
#   if keycomand == ord('q'):
#     break

# cap.release()
# cv2.destroyAllWindows()

  return key

