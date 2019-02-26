class Cipher:
    def __init__(self, codestring):

    	self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    	self.code = {b:a for (a,b) in zip(codestring.upper(), self.alphabet)}
    	self.inverse = {a:b for (a,b) in zip(codestring.upper(),self.alphabet)}
        
    def encode(self, plaintext):
        return "".join([self.code[c] if c.isalpha() else c for c in plaintext.upper()])

    def decode(self, ciphertext):
        return "".join([self.inverse[c] if c.isalpha() else c for c in ciphertext.upper()])
