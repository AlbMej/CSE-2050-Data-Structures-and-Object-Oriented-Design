from words import wordlist
from cipher import Cipher
#wordlist = list(wordlist)
class CipherCracker:
    def __init__(self, ciphertext):
        """
        The constructor takes a ciphertext that is assumed to have a preamble
        of 30 characters that contains the codeword.

        The preamble is removed from the ciphertext and stored separately.
        When we decode the message, we will omit the preamble.
        """
        self.preamble = ciphertext[:30]
        self.ciphertext = ciphertext[30:]

    def decode(self, i, j):
        """
        Attempts to decode the message using self.preamble[i:j] as the codeword.
        Returns the resulting string.
        """
        """
        codeword = Cipher(self.preamble[i:j])
        return codeword.decode(self.ciphertext)
        """             
        return Cipher(self.preamble[i:j]).decode(self.ciphertext) #One liner

    def quality(self, i, j):
        """
        Decodes the message using self.preamble[i:j] as the codeword and returns
        a number that gives an indication of how many of the words in the
        decoded string are real words.  It does this by checking if the words
        are in the `wordlist` variable imported from `words.py`.

        There are several ways this could be done.  The most important thing is
        that for a real message, the correct values of i and j should give
        a higher output than other values.
        """
        """ #Basic for-loop without having to turn wordlit into list O(n) time. 
        messages = self.decode(i, j).split()
        count = 0
        for i in messages:
            if i in wordlist:
                count += 1
        return count
        """
        #messages = self.decode(i,j).split()
        #return sum([wordlist.count(i) for i in messages]) #2 liner
        return sum([1 for i in self.decode(i,j).split() if i in wordlist]) #One liner 

    def mostlikelycodeword(self):
        """
        Return the codeword that has the highest quality score among all
        substrings of the preamble.
        """
        best, first_index, last_index = 0,0,0
        for i in range(31):
        	for j in range(i,31):
        		current = self.quality(i,j)
        		if current > best:
        			best, first_index, last_index = current, i, j
        return self.preamble[first_index:last_index]

    def mostlikelydecode(self):
        """
        Return the decoded message that you get by decoding with the most
        likely codeword.
        """
       	return Cipher(self.mostlikelycodeword()).decode(self.ciphertext)