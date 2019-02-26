class Cipher:
    def __init__(self, codestring):
    	self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    	self.codestring = codestring + "".join([c for c in 'ZYXWVUTSRQPONMLKJIHGFEDCBA' if c not in codestring])
    	self.code = {b:a for (a,b) in zip(self.codestring.upper(), self.alphabet)}
    	self.inverse = {a:b for (a,b) in zip(self.codestring.upper(),self.alphabet)}
        
    def encode(self, plaintext):
        return "".join([self.code[c] if c.isalpha() else c for c in plaintext.upper()])

    def decode(self, ciphertext):
    	return "".join([self.inverse[c] if c in self.inverse else c for c in ciphertext.upper()])

"""c = Cipher("A")
print(c.encode("ABCDEF"), "AZYXWV")
c = Cipher("CBA")
print(c.encode("HELLO"), "VYRRO")"""
