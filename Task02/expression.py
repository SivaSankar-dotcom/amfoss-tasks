import cv2
import pytesseract

image = cv2.imread('add.png') # Load the image

expression = pytesseract.image_to_string(image)   # Use pytesseract to extract text from the image

result = eval(expression)  # Remove any whitespace and evaluate the expression

print("the result of the expression is",result)
