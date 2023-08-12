from translator import Translator

class TextProcessor:
    def __init__(self, language = 'en', translator = None):
        self.language = language
        self.translator = translator
        assert translator or language == 'en'

    def __extract_text(self, path_to_file):
        with open(path_to_file) as file:
            text = file.read()
        return text

    def __preprocess(self, text):
        text = text.replace('\n','')
        return text

    def process(self, path_to_file):
        text = self.__extract_text(path_to_file)
        text = self.__preprocess(text)
        if self.language != 'en':
            text = self.translator.translate(text)
        return text

if __name__ == "__main__":
    translator = Translator(language = 'ru')
    processor = TextProcessor( language = 'ru', translator = translator)
    text = processor.process('texts/text_rus.txt')
    print(text)
