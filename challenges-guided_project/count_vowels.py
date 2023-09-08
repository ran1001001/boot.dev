def count_vowels(text):
    totalVowels = 0
    vowels = {"a", "e", "i", "o", "u"}
    for letter in text:
        if letter.lower() in vowels:
            totalVowels += 1
    return totalVowels


def test(text):
    vowels = count_vowels(text)
    print(f"Text: {text}")
    print(f"Vowels: {vowels}")
    print("---")


test(
    "Building a job-ready portfolio of coding projects doesn't happen overnight, but if you're like most self-taught developers, you've likely built up a nice collection of todo apps, calculators, and other toy programs. Here's the thing, applications for end-users are great, but I'm here to convince you that adding a library to your portfolio will make you much more hireable."
)
test(
    "Applications are normal programs. They start up and do some stuff. They have an entry point like a main() function. On the other hand, a library (aka package), consists of some code intended to be used in other programs. If you've ever used go get, npm install, or pip install, then you've included a 3rd party library in your code."
)
