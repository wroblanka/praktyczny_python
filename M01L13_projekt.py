### 🔴 Projekt

# Napisz dla BBC program sprawdzający złożoność artykułów i wpisów, dzięki czemu pracę dziennikarzy będzie można sparametryzować i automatycznie ustalić, czy piszą teksty proste i łatwe w zrozumieniu. Policz jaka jest średnia długość słów i wyświetl rezultat.

# Podpowiedzi:

#words = len(text.split())  # liczba słów

# a = 9
# b = 3
# division = a / b
# print(division)

# Aby policzyć średnią długość słowa, możesz bazować na liczbie wszystkich znaków oraz liczbie słów.

text = input("Please copy paste BBC text for analysis:")
words = len(text.split())
text_total_lenght= len(text)
text_words_avg_lenght = text_total_lenght / words
print("This text has average words lenght", text_words_avg_lenght, "characters.")
