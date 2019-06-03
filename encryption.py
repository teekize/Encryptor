"""this module is an encryption trial"""
from codez import encryptors,decryptors
from random import randint



class Encryption:
    @staticmethod
    def enc (word, key=None):
        new_letter =[]
        if key ==None:
            for letter in word.lower():
                enc_l = encryptors.get(letter)
                new_letter.append(enc_l)
            
            n= "".join(new_letter)
            return n
        elif key == '044':
            for letter in word.lower():
                enc_l = encryptors.get(letter)
                new_letter.append(enc_l)
            new_letter.reverse()
            n= "".join(new_letter)
            return n
            # for num in range(len(new_letter)):
            #     n = new_letter[0] + new_letter[1]
            # ''.join()
    @staticmethod
    def deco (enc_w, key=None):
        new_letter =[]
        lv=[]
        if key== None:
            for letter in enc_w:
                enc_l = decryptors.get(letter)
                new_letter.append(enc_l)
            
            n= "".join(new_letter)
            return n
        elif key=='044':
            # l =str(enc_w).split()
            # print(l)
            for letter in enc_w:
                new_letter.append(letter)

            new_letter.reverse()
            new_wo= "".join(new_letter)
            # print(new_wo)
            for letter in new_wo:
                enc_l = decryptors.get(letter)
                
                lv.append(enc_l)
            
            n= "".join(lv)
            return n


n=Encryption.enc ('I have first identified that the articles in the given website are' )
m=Encryption.deco('yF1sy5qZ/yes0ymqhsy85s0qsZy6|q5F1sy85s5185s[yq=q50y[qs5ZFq=sym18sq')

print(f"encoded word is  {n}")
print(f"decoded word is {m}")