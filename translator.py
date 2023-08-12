from tqdm.auto import tqdm
from googletrans import Translator as GoogleTranslator

class Translator:
    def __init__(self, language):
        self.translator = GoogleTranslator()
        self.language = language

    def translate_sentence(self, sentence):
        translation = ''
        try:
            translation = self.translator.translate(sentence, src=self.language).text
        finally:
            return translation

    def translate(self, text):
        sentences = text.split('.')
        translated_sentences = []
        pb = tqdm(sentences, leave=True)
        pb.set_description('Translating sentences...')
        for sentence in pb:
            translated_sentence = self.translate_sentence(sentence)
            translated_sentences.append(translated_sentence)
        return '.'.join(translated_sentences)


if __name__ == "__main__":
    translator = Translator('ru')
    print(translator.translate('Привет. Мир!'))