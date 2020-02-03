import pytesseract
from PIL import Image
import json
import os

import cv2

with open('config.json','r') as configf:
    config = json.load(configf)
    imageDir = config['imageDir']
    txtDir = config['txtDir']
    threshPicDir = config['threshPicDir']
    for key in config:
        Dir = config[key]
        if not os.path.isdir(Dir):
            os.mkdir(Dir)
            print('\'' + Dir + '\' is missing ~ but we created!')

print('processing...')

imageFiles = os.listdir(imageDir)
for imageFile in imageFiles:
    imageName = imageDir + imageFile
    txtName = txtDir + imageFile.split('.')[0] + '.txt'
    threshName = threshPicDir + imageFile

    img = cv2.imread(imageName)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgGray, 120, 255, cv2.THRESH_BINARY)
    cv2.imwrite(threshName, thresh)
    
    print(imageName + ' is being processed.')
    text = pytesseract.image_to_string(thresh, lang='chi_sim')
    with open(txtName, 'w') as txtf:
        txtf.write(text)


