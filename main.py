from coder import Coder
from galois import Galois


if __name__ == '__main__':
    gallois = Galois()
    coder = Coder(gallois)

    text = "AB"
    coder.RS_coder(text)