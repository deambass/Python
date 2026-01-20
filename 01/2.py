
from langdetect import detect


text_1 = "Hello World"
text_2 = "Привет мир "
text_3 = "Goedenmorgen "

print(detect(text_1))
print(detect(text_2))
print(detect(text_3))
