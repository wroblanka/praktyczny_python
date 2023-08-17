# Jesteś konsultantem działającym dla Niebezpiecznika - polskiego lidera cyberbezpieczeństwa. Napisz program, który będzie dokonywał audytu bezpieczeństwa u klientów Niebezpiecznika - jesteś odpowiedzialny za moduł sprawdzający złożoność haseł i generujący raport z rekomendacjami. 
#
# 1. Poproś użytkownika o hasło, a następnie sprawdź, czy spełnia ono reguły bezpieczeństwa.
# 2. Hasło powinno mieć minimum jedną małą literę, jedną wielką literę i jeden znak specjalny.
# 3. Hasło nie może zawierać spacji!  (wewnętrzny wymóg klienta wynikający z ograniczeń ich systemu teleinformatycznego)
# 4. Hasło musi mieć minimum 8 znaków.
# 5. Jeśli hasło jest niepoprawne, wyświetl raport w punktach co należy zmienić.

# PROJEKT
counter = 0

password = input("Please input PASSWORD :")

print("RAPORT:")

if len(password) >= 8:
    print("Your password is long enough")
else:
    print("Your password is NOT long enough! minimum 8 passwordacters") 

for char in password:
    if char.isspace()==False:
        counter += 1
    if char.isspace()==True:
        print("don't use white characters")
    if char.islower()==True: 
        counter += 1
    if char.islower()==False:
        print("use lowcase")        
    if char.isupper()== True:
        counter += 1
    if char.isupper()== False:
        print("use uppercase")
    if not char.isdigit()==True:
        special_character = True   
        counter += 1  
    else:
        special_character = True
        print("Please use at least one special character") 


# print(counter)
          
print("RESULT:")
if counter == 4:
    print("Your Password is safe")
else:
    print("Please correct password according to Report")
    
