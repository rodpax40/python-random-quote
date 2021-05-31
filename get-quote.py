import random

def roden():
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = 15
    rnd = random.randint(0, last)
    print(quotes[rnd])

    last = 15
    rnd = random.randint(0, last)
    print(quotes[rnd])


if __name__== "__main__":
  roden()
