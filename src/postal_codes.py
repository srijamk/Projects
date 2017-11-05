class PostalCodes():
    province_to_postal_code = {
    "Newfoundland": "A",
    "Nova Scotia": "B",
    "Prince Edward Island": "C",
    "New Brunswick": "E",
    "Quebec": ("G", "H", "J"),
    "Ontario": ("K", "L", "M", "N", "P"),
    "Manitoba": 'R',
    "Saskatchewan": "S",
    "Alberta": "T",
    "British Columbia": "V",
    "Nunavut": "X",
    "Northwest Territories": "X",
    "Yukon": "Y"
    }
    def get_province(self, postal_code):
        if postal_code[0] in self.province_to_postal_code.values():
            for key in self.province_to_postal_code:
                if postal_code[0] in self.province_to_postal_code[key] and postal_code[1] == 0:
                    return "Rural address in %s" % key
                elif postal_code[0] in self.province_to_postal_code[key] and postal_code[1] != 0:
                    return "Urban address in %s" % key
        else:
            return "Invalid postal code"

    def main(self):
        # Should return 'Rural address in Northwest Territories'
        return self.get_province("X0A 1B2") + "\n" + self.get_province("T2N 1N4")
        # Should return 'Urban address in Alberta'

print PostalCodes().main()
