from PIL import Image

index = []
stack = []

islandcounter = 0

recursion = False
x = 1
y = 1
stop = False


def stackAdd(x, y):
    if x > 0 and y > 0 and x < im.width and y < im.height:
        if index[x][y] == 0:
            # pixels[y * img.width + x] = (255, 255, 0)
            imf.putpixel((x, y), (255, 255, 0))
            stack.append([x, y])

im = Image.open("assets/vector-world-map-v2.2-blank.png")
imf = im.copy()

index = [[0 for y in range(im.height + 2)] for x in range(im.width + 2)]

while (stop == False):

    if recursion == False:

        if index[x][y] == 0:
            index[x][y] = 1
            # imgfinal.pixels[y * img.width + x] = color(0, 0, 255)
            # pixels[y * img.width + x] = color(0, 0, 255)
            imf.putpixel((x, y), (0, 0, 255))

            if im.getpixel((x, y)) == (0, 0, 0):

                # imgfinal.pixels[y * img.width + x] = color(255, 0, 0)
                # pixels[y * img.width + x] = color(255, 0, 0)
                imf.putpixel((x, y), (255, 0, 0))

                index[x][y] = 0
                stackAdd(x, y)
                recursion = True

        x += 1
        if x == im.width - 2:
            x = 0
            y += 1
            if y == im.height - 2:
                stop = True
    else:

        if len(stack) != 0:
            point = stack.pop()

            if index[point[0]][point[1]] == 0:
                index[point[0]][point[1]] = 1
                # imgfinal.pixels[y * img.width + x] = color(0, 0, 255)
                # pixels[y * img.width + x] = color(0, 0, 255)
                imf.putpixel((x, y), (0, 0, 255))

                # print(str(point[0]) + " - " + str(point[1]) + "#" +
                # str(im.width) + " - " + str(im.height))

                if im.getpixel((point[0], point[1])) == (0, 0, 0):

                    # imgfinal.pixels[point[1] * img.width + point[0]] = color(255, 0, 0)
                    # pixels[point[1] * img.width + point[0]] = color(255, 0, 0)
                    imf.putpixel((x, y), (255, 0, 0))

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
            islandcounter += 1

imf.show()
print(islandcounter);
