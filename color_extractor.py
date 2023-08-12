import re
import json
from text_processor  import TextProcessor

class ColorExtractor:
    def __init__(self, colors):
        self.__colors = colors
        self.__pattern = re.compile('|'.join(f'\s{color}\s' for color in self.__colors))

    def extract(self, text):
        text = text.lower()
        matches = self.__pattern.findall(text)
        matches = [color.strip() for color in matches]
        return matches


if __name__ == "__main__":
    processor = TextProcessor()
    text = processor.process('text.txt')

    with open('colors.json') as file:
        colors = json.load(file)
    extactor = ColorExtractor(colors)
    extracted_colors = extactor.extract(text)
    print(extracted_colors)





