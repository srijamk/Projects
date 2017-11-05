class UniqueChars():
    def get_unique_characters(self, message):
        return len(set(message))

    def main(self):
        # Should return 10
        return self.get_unique_characters("hello, world!")

print UniqueChars().main()
