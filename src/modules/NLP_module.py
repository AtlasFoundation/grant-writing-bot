import spacy


class NLPModule:
    def __init__(self, config: Config):
        self.config = config
        self.nlp = spacy.load(self.config.nlp_model)

    def extract_keywords(self, text: str):
        """
        Extract keywords from text
        """
        doc = self.nlp(text)
        keywords = [token.text for token in doc if token.is_stop !=
                    True and token.is_punct != True]
        return keywords
