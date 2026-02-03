import string

text = input("Введіть рядок: ")

clean_text = ""
for ch in text:
    if ch not in string.punctuation:
        clean_text = clean_text + ch

words = clean_text.split()

hashtag = "#"
for w in words:
    hashtag = hashtag + w.capitalize()

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
