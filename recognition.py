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
  result = ''
  # img = cv2.imread('') #テスト用
  # im = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #テスト用

  im = post
  print(im)

  
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
        minNeighbors = 2,
        minSize=(30,30)
  )

  for(x,y,w,h) in faces:
    cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 2)
    id, confidence = recognizer.predict(im[y:y+h,x:x+w])
    id = names[id]
    confidence = "  {0}".format(round(100 - confidence))


  # print(id)
  # print(confidence)

  #%%
  """最終判断"""
  if result >=1:
    key = 'Danger'
    if id == 'mama' or id == 'papa':
      key = 'Super_Danger'
      telcoll.coll()
    else:
      key = 'Danger'

  elif id == 'mama' or id == 'papa':
    key = 'Super_Danger'
    telcoll.coll()

  else:
    key = 'Noproblem'

  print(key)

  return key


