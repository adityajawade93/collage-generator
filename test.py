import imgkit
from helpers import generateIndexFile

imgArray = ['testImg.jpg', 'testImg.jpg']

html = generateIndexFile.generateHtml(imgArray)

html_file = open("test.html", "w")
html_file.write(html)
html_file.close()

imgkit.from_file('test.html', 'out.jpg')