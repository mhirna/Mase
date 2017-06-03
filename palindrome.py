from linkedstack import LinkedStack

class palindrom_ADT:

    def __init__(self, filename):
        self.filename = filename
        self.words = LinkedStack()
        self.test = []
        self.palindroms = []

    def read_dict(self):
        with open(self.filename, encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            for i in lines:
                self.words.push(i.split()[0])
                self.test.append(i.split()[0])

    def check_palindrome(self):
        while not self.words.isEmpty():
            is_palindrome = True
            word = self.words.peek()
            l = len(word)
            mid = l // 2 + l % 2
            if l < 2:
                is_palindrome = False
            for i in range(mid):
                if word[i] != word[l - i - 1]:
                    is_palindrome = False
            if is_palindrome:
                self.palindroms.append(word)
            self.words.pop()


    def write_palindromes(self, s):
        f = open(s, "w", encoding="utf-8")
        for i in range(len(self.palindroms) - 1, 0, -1):
            f.write(self.palindroms[i] + "\n")
        f.close()

base = palindrom_ADT("base.lst")
base.read_dict()
base.check_palindrome()
base.write_palindromes("palindrome_uk.txt")
words = palindrom_ADT("words.txt")
words.read_dict()
words.check_palindrome()
words.write_palindromes("palindrome_en.txt")
