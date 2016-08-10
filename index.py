from PIL import Image
import sys

sys.setrecursionlimit(1000000)

index = []
islandcounter = 0


def checkPixel(x, y):

    #print(str(x) + " - " + str(y))
    if x > 0 and y > 0 and x < im.width and y < im.height:
        #print(str(x) + " - " + str(y) + "#" +
        #      str(im.width) + " - " + str(im.height))
        if index[x][y] == 0:
            index[x][y] = 1
            if im.getpixel((x, y)) == (0, 0, 0):
                getPixelNeightboor(x, y)
        # print("\n")
        # sys.stdout.flush()


def getPixelNeightboor(x,  y):
    checkPixel(x - 1, y - 1)
    checkPixel(x - 1, y)
    checkPixel(x - 1, y + 1)
    checkPixel(x, y - 1)
    checkPixel(x, y + 1)
    checkPixel(x + 1, y - 1)
    checkPixel(x + 1, y)
    checkPixel(x + 1, y + 1)

im = Image.open("data/vector-world-map-v2.2-blank.png")
px = im.load()

index = [[0 for y in range(im.height + 2)] for x in range(im.width + 2)]
#print(len(index))
#print(len(index[0]))

for x in range(1, im.width - 1):
    for y in range(1, im.height - 1):
        checkPixel(x, y)


# im.show()
