import string
"""
Creates encrypted ciphertext from plaintext,
Takes string and cipher code (integer), and matches string index from plaintext to ciphertext,
Returns matched string from ciphertext.
"""


def build_coder(shift):
    original = string.ascii_lowercase
    shifted_string = original[shift:26] + original[:shift]
    return shifted_string


def apply_coder(name, function):
    original = string.ascii_lowercase
    word = ''
    for i in name:
        if i in function:
            word += (function[original.index(i)])
        elif i in function.upper():
            word += (function.upper()[original.upper().index(i)])
        else:
            word += (name[name.index(i)])
    return word


def applyShift(name, shift):
    return apply_coder(name, build_coder(shift))


f = "Tkmu Pvyboi sc k widrsmkv mrkbkmdob mbokdon, led rkc bozybdonvi xofob zkccon k mvkcc."
l = 16
print(applyShift(f, l))
