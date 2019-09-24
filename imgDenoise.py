import matplotlib.pyplot as plt
import numpy as np

# Load Images 
def loadImg(file):
    img = plt.imread(file)
    new = np.zeros((img.shape[0],img.shape[1]))
    return img, new

# Local Averaging Filter
def local(file):
    img,new = loadImg(file)
    num=0
    count=0
    for row in range(0,img.shape[0]):
        for col in range(0,img.shape[1]):
            for i in img[row:row+3,col:col+3]:
                for l in i:
                    num=num+l
                    count=count+1
            fin = num/count
            new[row,col]=(fin)
            num=0
            count=0
    return new

# Median Filter
def median(file):
    img,new = loadImg(file)
    for row in range(0,img.shape[0]):
        for col in range(0,img.shape[1]):
            lst=[]
            for i in img[row:row+3,col:col+3]:               
                for l in i:
                    lst.append(l)
            lst.sort()
            if len(lst)>=9:
                new[row,col] = (lst[int((len(lst)+1)/2)])
            else:
                new[row,col] = (lst[int((len(lst)-1)/2)])
            del lst
    return new


plt.subplot(231)
plt.imshow(plt.imread("gaussian.png"), cmap = "gray")
plt.title('Gaussian Noise Image')

plt.subplot(232)
plt.imshow(local("gaussian.png"), cmap = "gray")
plt.title('Gaussian Noise Image - Local Averaging')

plt.subplot(233)
plt.imshow(median("gaussian.png"), cmap = "gray")
plt.title('Gaussian Noise Image - Median Filtering')

plt.subplot(234)
plt.imshow((plt.imread("saltpepper.png")),cmap = "gray")
plt.title('Salt & Pepper Noise Image')

plt.subplot(235)
plt.imshow(local("saltpepper.png"), cmap = "gray")
plt.title('Salt & Pepper Noise Image - Local Averaging')

plt.subplot(236)
plt.imshow(median("saltpepper.png"), cmap = "gray")
plt.title('Salt & Pepper Noise Image - Median Filtering')

plt.show()
