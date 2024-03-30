#import re

class TextFilter():
    def __init__(self):
        pass

    def replace_segment(string, old_substring, new_substring):
        modified_string = string.replace(old_substring, new_substring)
        return modified_string