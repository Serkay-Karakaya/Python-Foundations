"""name = "Serkay"
surname = "Karakaya"""
""" 
print("My name is {} {}".format(name,surname)) # My name is Serkay Karakaya
print("My name is {0} {1}".format(name,surname)) # My name is Serkay Karakaya
print("My name is {1} {0}".format(name,surname)) # My name is Karakaya Serkay
print("My name is {n} {s}".format(n=name,s=surname)) # My name is Serkay Karakaya
print(f"My name is {name} {surname}") # My name is Serkay Karakaya
"""
"""
result = 200/700
print("The result is {}".format(result)) # The result is 0.285...  
print("The result is {r:1.2}".format(r=result)) # The result is 0.29
print("The result is {r:1.5}".format(r=result)) # The result is 0.28571
"""
#----------------------------------------------------------
"""
website = "http://www.serkaykarakaya.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
print(len(course)) # Toplam uzunluk
print(website[7:10]) #www yazar
print(website[26:]) #com yazar
print(course[:15]) #ilk 15 karakter
print(course[-15:]) #son 15 karakter
print(course[::-1]) #tersten yazdırma
"""
#----------------------------------------------------------
"""
name,surname,age,job = "serkay","kara",21,"yazılımcı"
print("Benim adım "+name+" "+surname+", " + "Yaşım " +str(age)+" ve mesleğim "+ job)
"""
#----------------------------------------------------------
"""
print("abc"*3) #abc yanyana 3 defa yazılır
print("Hello word".replace("w","W")) #W büyür, Hello Word yazar.
"""

