import sys

class ParityBits():
    def get_parity_bit(self, bits):
        parity_bit = 1
        if bits.count(1) % 2 == 0:
            parity_bit = 0
        return parity_bit

first_bit = raw_input("Enter a list of 8 bits: ")
bits = []
bits.append(first_bit)
while first_bit != "":
    next_bit = raw_input("Enter next bit: ")
    if next_bit != "":
        bits.append(next_bit)
    if len(bits) != 8:
        print "Invalid string."
        sys.exit()
    else:
        GivenBitList = ParityBits()
        print GivenBitList.get_parity_bit(bits)
