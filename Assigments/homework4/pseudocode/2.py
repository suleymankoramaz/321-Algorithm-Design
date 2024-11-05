def findBrightestPixel(image):
    n = image.length    #number of columns
    m = image[0].length #number of rows

    row, col = 0, 0

    while True:

        max_brightness = image[row][col]
        brightest_neighbor = None
        
        if row > 0 and image[row - 1][col] > max_brightness:
            max_brightness = image[row - 1][col]
            brightest_neighbor = (row - 1, col)

        if row < n - 1 and image[row + 1][col] > max_brightness:
            max_brightness = image[row + 1][col]
            brightest_neighbor = (row + 1, col)

        if col > 0 and image[row][col - 1] > max_brightness:
            max_brightness = image[row][col - 1]
            brightest_neighbor = (row, col - 1)

        if col < m - 1 and image[row][col + 1] > max_brightness:
            max_brightness = image[row][col + 1]
            brightest_neighbor = (row, col + 1)

        if brightest_neighbor is None:
            return (row, col)
        else:
            row, col = brightest_neighbor