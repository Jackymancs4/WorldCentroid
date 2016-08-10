import cv2
import random
import numpy as np

#cv2.startWindowThread()

index = []
stack = []

islandcounter = 0

recursion = False

x = 1
y = 1
stop = False


def stackAdd(x, y):
    if x > 0 and y > 0 and x < height and y < width:
        if index[x][y] == 0:
            #imf[x, y] = [255, 255, 0]
            stack.append([x, y])


def checkPixel(x, y, r):
    #imf[x, y] = [0, 0, 255]
    index[x][y] = 1

    #if not(np.array_equal(im[x, y], [255, 255, 255])):
    if np.array_equal(im[x, y], [0, 0, 0]):
        #imf[x, y] = [255, 0, 0]
        imf[x, y] = nowcol

        if r == True:
            global recursion
            recursion = True

        stackAdd(x - 1, y - 1)
        stackAdd(x - 1, y)
        stackAdd(x - 1, y + 1)
        stackAdd(x, y - 1)
        stackAdd(x, y + 1)
        stackAdd(x + 1, y - 1)
        stackAdd(x + 1, y)
        stackAdd(x + 1, y + 1)

    #elif not(np.array_equal(im[x, y], [255, 255, 255])):
        #imf[x, y] = [255, 255, 255]

im = cv2.imread('data/vector-world-map-v2.2-blank.png')
#im = cv2.resize(im, (0, 0), fx=0.2, fy=0.2)
imf = im.copy()

height, width, nothing = im.shape

index = [[0 for y in range(width + 2)] for x in range(height + 2)]

framecounter = 0

nowcol = [random.randrange(255), random.randrange(255), random.randrange(255)]

while stop == False:

    #if framecounter % 1500 == 0:
    #    cv2.imshow('', imf)
    #    cv2.waitKey(1)

    framecounter += 1

    if recursion == False:

        if index[x][y] == 0:
            checkPixel(x, y, True)

        y += 1
        if y > width - 2:
            y = 0
            x += 1
            if x > height - 2:
                stop = True
    else:

        if len(stack) != 0:
            point = stack.pop()

            if index[point[0]][point[1]] == 0:

                checkPixel(point[0], point[1], False)

        else:
            recursion = False
            print("bitch - " + str(islandcounter) +
                  " - " + str(x) + " - " + str(y))

            nowcol = [random.randrange(255), random.randrange(
                255), random.randrange(255)]

            islandcounter += 1

print(islandcounter)

cv2.imwrite("output/img2.png", imf)

cv2.waitKey(0)
