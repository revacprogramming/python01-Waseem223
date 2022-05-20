# Strings
text = "X-DSPAM-Confidence:    0.8475"
def find():
    b=text.find('0')
    print(float(text[b:]))
find()
