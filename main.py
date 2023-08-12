import os
import json
from translator import Translator
from text_processor import TextProcessor
from color_extractor import ColorExtractor
from portrait_constructor import construct_portrait


class TextColorer:
    def __init__(self, path_to_colors='colors.json', language='en'):
        with open(path_to_colors) as file:
            self.colors = json.load(file)
        self.__translator = Translator(language=language)
        self.__processor = TextProcessor(language=language, translator=self.__translator)
        self.__extractor = ColorExtractor(self.colors)

    def __make_path_to_portrait(self, text_filename):
        os.makedirs('portraits', exist_ok=True)
        portrait_filename = text_filename.replace('txt', 'png')
        return os.path.join('portraits', portrait_filename)

    def make_portrait(self, path_to_text, path_to_portrait=None):
        text_filename = os.path.split(path_to_text)[-1]
        path_to_portrait = path_to_portrait or self.__make_path_to_portrait(text_filename)
        text = self.__processor.process(path_to_text)
        extracted_colors = self.__extractor.extract(text)
        portrait = construct_portrait(extracted_colors)
        portrait.savefig(path_to_portrait)
        print(f'Color portrait of the book "{text_filename}" successfully saved to "{path_to_portrait}"')


if __name__ == "__main__":
    colorer = TextColorer(language='ru')
    colorer.make_portrait('texts/12.txt')
