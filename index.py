import cv2
import random
import numpy as np

cv2.startWindowThread()

index = []
stack = []

islandcounter = 0

recursion = False
x = 1
y = 1
stop = False


def stackAdd(x, y):
    if x > 2 and y > 2 and x < height - 1 and y < width - 1:
        if index[x][y] == 0:
            imf[x, y] = [255, 255, 0]
            stack.append([x, y])

im = cv2.imread('data/vector-world-map-v2.2-blank.png')
im = cv2.resize(im, (0, 0), fx=0.2, fy=0.2)
imf = im.copy()

height, width, nothing = im.shape

index = [[0 for y in range(width + 2)] for x in range(height + 2)]

framecounter = 0

while stop == False:

    if framecounter % 1500 == 0:
        cv2.imshow('', imf)
        cv2.waitKey(1)

    framecounter += 1

    if recursion == False:

        if index[x][y] == 0:

            # visited node
            index[x][y] = 1
            imf[x, y] = [0, 0, 255]

            if np.array_equal(im[x, y], [0, 0, 0]):
                imf[x, y] = [255, 0, 0]
                recursion = True

                stackAdd(x - 1, y - 1)
                stackAdd(x - 1, y)
                stackAdd(x - 1, y + 1)
                stackAdd(x, y - 1)
                stackAdd(x, y + 1)
                stackAdd(x + 1, y - 1)
                stackAdd(x + 1, y)
                stackAdd(x + 1, y + 1)

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

                index[point[0]][point[1]] = 1
                imf[point[0], point[1]] = [0, 0, 255]

                if np.array_equal(im[point[0], point[1]], [0, 0, 0]):

                    imf[point[0], point[1]] = [255, 0, 0]

                    stackAdd(point[0] - 1, point[1] - 1)
                    stackAdd(point[0] - 1, point[1])
                    stackAdd(point[0] - 1, point[1] + 1)
                    stackAdd(point[0], point[1] - 1)
                    stackAdd(point[0], point[1] + 1)
                    stackAdd(point[0] + 1, point[1] - 1)
                    stackAdd(point[0] + 1, point[1])
                    stackAdd(point[0] + 1, point[1] + 1)

        else:
            recursion = False
            print("bitch - "+str(islandcounter)+" - "+str(x)+" - "+str(y))


            islandcounter += 1

#cv2.waitKey(0)
print(islandcounter)
