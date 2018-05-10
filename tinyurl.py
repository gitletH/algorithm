# href: https://leetcode.com/problems/encode-and-decode-tinyurl/description/

class Codec:
    chars = [i for i in range(10)]
    chars.extend(chr(i) for i in range(ord('A'), ord('Z') + 1))
    chars.extend(chr(i) for i in range(ord('a'), ord('z') + 1))

    
    def __init__(self):
        self.m = {}
        self.ctr = 0
    

    @staticmethod
    def foo(n):
        pass

    @staticmethod
    def bar(str):
        pass

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))