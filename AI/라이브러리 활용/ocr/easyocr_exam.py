import easyocr

reader = easyocr.Reader(['en', 'ko'])

results = reader.readtext('NEWS2x.png')

print(results)
