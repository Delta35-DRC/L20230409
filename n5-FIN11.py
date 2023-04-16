import cv2
from PIL import Image

print('note that latest result will overwrite previous')
path = input('source path: ')
path_glasses = input('glasses path: ')
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
human_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(path)

cat_face = cat_face_cascade.detectMultiScale(image)
human_face = human_face_cascade.detectMultiScale(image)
img = Image.open(path)
glasses = Image.open(path_glasses)
img = img.convert('RGBA')
glasses = glasses.convert('RGBA')

for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    img.paste(glasses, (x, int(y+h/4)), glasses)

for (x, y, w, h) in human_face:
    glasses = glasses.resize((w, int(h/3)))
    img.paste(glasses, (x, int(y+h/4)), glasses)
    img.save('img_glasses.png')

img_done = cv2.imread('img_glasses.png')
cv2.imshow('img_glasses', img_done)
cv2.waitKey()
