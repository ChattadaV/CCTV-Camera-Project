import os

output=os.system('sudo apt install -y tesseract-ocr') #use -y to confirm 'yes' to 'Do you want to continue(y/n)?' question
output=os.system('sudo apt install -y libtesseract-dev')

output=os.system('pip install virtualenv')
output=os.system('virtualenv env')
output=os.system('source activate env/activate/bin')
output=os.system('pip install pillow')
output=os.system('pip install pytesseract')


#output=os.system('sudo pip install pytesseract')