class HexadecimalConversion():
    def hex2int(self, hexa):
        if ord(hexa.upper()) <= 57:
            return hexa
        else:
            return ord(hexa) - 55

    def int2hex(self, integer):
        if integer <= 9:
            return integer
        elif 9 < integer <= 15:
            return chr(integer + 55)

    def main(self):
        hex_or_int = raw_input("Do you have a hex or integer? > ")
        if hex_or_int == "hex":
            hexa = raw_input("Enter a hexadecimal digit: ")
            print self.hex2int(hexa)
        else:
            integer = int(raw_input("Enter an integer: "))
            print self.int2hex(integer)

if __name__ == '__main__':
    HexadecimalConversion().main()
