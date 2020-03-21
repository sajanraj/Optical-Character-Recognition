# -*- coding: utf-8 -*-
# import the necessary packages


# construct the argument parse and parse the arguments
def ocr(imgdata,pan,preprs):
    print('path1=',imgdata)
    from PIL import Image
    import pytesseract
    import cv2
    import os
    path=os.getcwd()
    print('pathos=',str(path))
    from pdf2image import convert_from_path
    # load the example image and convert it to grayscale
    if imgdata.lower().endswith(('.pdf')):
        filename = "{}.jpg".format(os.getpid())
        pages = convert_from_path(imgdata, 200)
        for page in pages:
            page.save(filename, 'JPEG')
        image = cv2.imread(filename)
    else:
        image = cv2.imread(imgdata)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the
    # image
    if preprs == "thresh":
        gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove
    # noise
    elif argspreprs == "blur":
        gray = cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)




    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    flagis=0
    text = text.lower()
    print(text)
    word = text.find(pan.lower())
    if (word > 0):
        flagis=1
    print(flagis)
    return text,flagis
    #Return url
    # show the output images
    #cv2.imshow("Image", image)
    #cv2.imshow("Output", gray)
    #cv2.waitKey(0)

