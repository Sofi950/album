
import os
import cv2

path = "Images/"
images = []


for archivo in os.listdir(path):
    
    images, extension = os.path.splitext(path)
    ext = ['.gif', '.png', '.jpg', '.jpeg'] 
for archivo in os.listdir(images):
    if ext in ['.gif', '.png', '.jpg', 'jpeg', ',jfif']

print(images)

path.append('111.jpg')
path.append('112.jpg')
path.append('113.jpg')
path.append('114.jpg')
path.append('115.jpg')
path.append('116.jpg')
path.append('117.jpg')
path.append('118.jpg')
path.append('119.jpg')
path.append('120.jpg')

count = len(images)
frame = cv2.imread(images[0])
frame.shape= width, height, channels
size = (width, height)
print(size)

out = cv2.VideoWriter('projecto.avi', cv2.VideoWriter_fourcc(*"DIVX"), 0.8, size)

for i in range(count):
    img = cv2.imread(images[i])
    out.write(img)

out.release()
print("Listo")
