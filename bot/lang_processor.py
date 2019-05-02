import konlpy
import nltk


class KoProcessor:

    def __init__(self, sentence=None):
        self.sentence = sentence

    def set_chunks(self, sentence):
        words = konlpy.tag.Twitter().pos(sentence)

        grammar = """
        NP: {<N.*>*<Suffix>?}
        VP: {<V.*>*}
        AP:{<A.*>*}
        """
        parser = nltk.RegexpParser(grammar)
        return parser.parse(words)

    def get_tree(self, sentence):
        self.chunks = self.set_chunks(sentence)
        return self.chunks

    def get_specific_tag(self, sentence, tag):
        if tag not in ['NP', 'VP', 'AP']:
            raise Exception('Not valid grammar tag')
        self.chunks = self.set_chunks(sentence)
        tag_all = []
        for subtree in self.chunks.subtrees():
            if subtree.label == tag:
                tag_all.extend((e for e in list(subtree)))
