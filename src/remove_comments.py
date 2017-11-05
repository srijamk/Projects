class Comments():
    def remove_comments(self, file_name, new_file_name):
        valid_lines = []
        with open(file_name, 'r') as f:
            for line in f:
                if "#" not in line:
                    valid_lines.append(str(line))

        with open(new_file_name, 'w') as f:
            for line in valid_lines:
                f.write(line)


print Comments().remove_comments('new_file.py', 'remove_comments_test.py')
