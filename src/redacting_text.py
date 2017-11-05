import re

class File():
    def redact_text(self, file_name, new_file_name, sensitive_words_file):
        words_list = []
        sensitive_words_list = []
        # Writes content of original file to new file
        with open(new_file_name, 'w') as redacted_text:
            with open(file_name, 'r') as old_file:
                all_text = old_file.read()
                redacted_text.write(all_text)

        # Replace method for sensitive words
        with open(new_file_name, 'r') as redacted_text:
            for line in redacted_text.readlines():
                line = filter(None, re.split("[, .\n-!?:]+", line))
                words_list.append(line)


        with open(sensitive_words_file, 'r') as sensitive_words:
            for word in sensitive_words.readlines():
                word = filter(None, re.split("[, .\n-!?:]+", word))
                sensitive_words_list.append(word)

        print sensitive_words_list
        for line in words_list:
            for word in line:
                for sensitive_word in sensitive_words_list:
                    if word == sensitive_word:
                        print word

print File().redact_text('new_file.py', 'redacted_text.txt', 'sensitive_words.txt')
