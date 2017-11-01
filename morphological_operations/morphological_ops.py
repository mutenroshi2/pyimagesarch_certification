class Palindrome:

    @staticmethod
    def is_palindrome(word):
        a = word.lower()
        print(a[::-1])
        return a == a[::-1]

print(Palindrome.is_palindrome('Deleveled'))