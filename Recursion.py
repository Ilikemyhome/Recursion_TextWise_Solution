'''
generate 

e , generat
et ,genera
eta , gener
etar, gene
etare , gen
etaren , ge
eterene , g

etareneg

'''

def reverserString(string):
    string = string.lower()

    if len(string) <= 1 :
        return string
    
    return string [-1] + reverserString(string[:-1])

s = "Hippopotomonstrosesquippedaliophobia"

print(reverserString(s))
    