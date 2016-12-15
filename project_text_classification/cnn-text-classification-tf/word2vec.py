import gensim

class Word2vec(object):

	def __init__(self, path_='../GoogleNews-vectors-negative300.bin.gz', binary=True):
		print("\nloading word2vec database")
		self.model = gensim.models.Word2Vec.load_word2vec_format(path_, binary=binary)
		print("\nloading done !")

	def isin(self, word):
		return (word in self.model.vocab)

	def get(self, word):
		if self.isin(word):
			return self.model[word]


if __name__ == '__main__':
	model = gensim.models.Word2Vec.load_word2vec_format('../GoogleNews-vectors-negative300.bin.gz', binary=True)
	w2v = Word2vec()
	while True:
		input_ = input("=>")
		print(input_ , ": ", w2v.isin(input_) ,"\n")

		if w2v.isin(input_):
			print(w2v.get(input_))