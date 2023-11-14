
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# geeft een numpy array terug, maar kan gebruikt worden alsof het een lijst is.
picture = mpimg.imread('modeloplossingen/IMG_0890.jpg')

dim_picture = [len(picture), len(picture[0])]
# Horizontale spiegeling:
picture_90 = []
for j in range(dim_picture[1]-1, -1, -1):
    pic_rij = []
    for i in range(dim_picture[0]):
        pic_rij.append(picture[i][j])
    picture_90.append(pic_rij)

plt.figure()
plt.imshow(picture_90)


# Horizontale spiegeling:
picture_horz = []
for i in range(dim_picture[0]):
    pic_rij = []
    for j in range(dim_picture[1]-1, -1, -1):
        pic_rij.append(picture[i][j])
    picture_horz.append(pic_rij)

plt.figure()
plt.imshow(picture_horz)


# puntspiegeling:
picture_punt = []
for i in range(dim_picture[0]-1, -1, -1):
    pic_rij = []
    for j in range(dim_picture[1]-1, -1, -1):
        pic_rij.append(picture[i][j])
    picture_punt.append(pic_rij)

plt.figure()
plt.imshow(picture_punt)


plt.imshow(picture)
