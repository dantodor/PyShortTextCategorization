import unittest
import shorttext

class TestVarNNEmbeddedVecClassifier(unittest.TestCase):
    def setUp(self):
		self.w2v_model = shorttext.utils.load_word2vec_model('data/text8_1000000_wordvectors', binary=False)  # load word2vec model
		self.trainclass_dict = shorttext.data.subjectkeywords()  # load training data    	

    def testCNNWordEmbedWithoutGensim(self):
  		# create keras model using `CNNWordEmbed` class
  		keras_model = shorttext.classifiers.frameworks.CNNWordEmbed(wvmodel=self.w2v_model, nb_labels=len(self.trainclass_dict.keys()), vecsize=100, with_gensim=False)

    	# create and train classifier using keras model constructed above
		main_classifier = shorttext.classifiers.VarNNEmbeddedVecClassifier(self.w2v_model, with_gensim=False, vecsize=100)
		main_classifier.train(self.trainclass_dict, keras_model, nb_epoch=2)

		# compute classification score
		score_vals = main_classifier.score('artificial intelligence')
		self.assertTrue(score_vals['mathematics']>0.0 and score_vals['physics']>0.0 and score_vals['theology']>0.0)

    def testDoubleCNNWordEmbedWithGensim(self):
  		# create keras model using `DoubleCNNWordEmbed` class
  		keras_model = shorttext.classifiers.frameworks.DoubleCNNWordEmbed(wvmodel=self.w2v_model, nb_labels=len(self.trainclass_dict.keys()), vecsize=100, with_gensim=True)

    	# create and train classifier using keras model constructed above
		main_classifier = shorttext.classifiers.VarNNEmbeddedVecClassifier(self.w2v_model, with_gensim=True, vecsize=100)
		main_classifier.train(self.trainclass_dict, keras_model, nb_epoch=2)

		# compute classification score
		score_vals = main_classifier.score('artificial intelligence')
		self.assertTrue(score_vals['mathematics']>0.0 and score_vals['physics']>0.0 and score_vals['theology']>0.0)

    def testDoubleCNNWordEmbedWithoutGensim(self):
  		# create keras model using `DoubleCNNWordEmbed` class
  		keras_model = shorttext.classifiers.frameworks.DoubleCNNWordEmbed(wvmodel=self.w2v_model, nb_labels=len(self.trainclass_dict.keys()), vecsize=100, with_gensim=False)

    	# create and train classifier using keras model constructed above
		main_classifier = shorttext.classifiers.VarNNEmbeddedVecClassifier(self.w2v_model, with_gensim=False, vecsize=100)
		main_classifier.train(self.trainclass_dict, keras_model, nb_epoch=2)

		# compute classification score
		score_vals = main_classifier.score('artificial intelligence')
		self.assertTrue(score_vals['mathematics']>0.0 and score_vals['physics']>0.0 and score_vals['theology']>0.0)

    def testCNNWordEmbedWithGensim(self):
  		# create keras model using `CNNWordEmbed` class
  		keras_model = shorttext.classifiers.frameworks.CNNWordEmbed(wvmodel=self.w2v_model, nb_labels=len(self.trainclass_dict.keys()), vecsize=100, with_gensim=True)

    	# create and train classifier using keras model constructed above
		main_classifier = shorttext.classifiers.VarNNEmbeddedVecClassifier(self.w2v_model, with_gensim=True, vecsize=100)
		main_classifier.train(self.trainclass_dict, keras_model, nb_epoch=2)

		# compute classification score
		score_vals = main_classifier.score('artificial intelligence')
		self.assertTrue(score_vals['mathematics']>0.0 and score_vals['physics']>0.0 and score_vals['theology']>0.0)

    def testCLSTMWordEmbedWithoutGensim(self):
  		# create keras model using `CLSTMWordEmbed` class
  		keras_model = shorttext.classifiers.frameworks.CLSTMWordEmbed(wvmodel=self.w2v_model, nb_labels=len(self.trainclass_dict.keys()), vecsize=100, with_gensim=False)

    	# create and train classifier using keras model constructed above
		main_classifier = shorttext.classifiers.VarNNEmbeddedVecClassifier(self.w2v_model, with_gensim=False, vecsize=100)
		main_classifier.train(self.trainclass_dict, keras_model, nb_epoch=2)

		# compute classification score
		score_vals = main_classifier.score('artificial intelligence')
		self.assertTrue(score_vals['mathematics']>0.0 and score_vals['physics']>0.0 and score_vals['theology']>0.0)

    def testCLSTMWordEmbedWithGensim(self):
  		# create keras model using `CLSTMWordEmbed` class
  		keras_model = shorttext.classifiers.frameworks.CLSTMWordEmbed(wvmodel=self.w2v_model, nb_labels=len(self.trainclass_dict.keys()), vecsize=100, with_gensim=True)

    	# create and train classifier using keras model constructed above
		main_classifier = shorttext.classifiers.VarNNEmbeddedVecClassifier(self.w2v_model, with_gensim=True, vecsize=100)
		main_classifier.train(self.trainclass_dict, keras_model, nb_epoch=2)

		# compute classification score
		score_vals = main_classifier.score('artificial intelligence')
		self.assertTrue(score_vals['mathematics']>0.0 and score_vals['physics']>0.0 and score_vals['theology']>0.0)

if __name__ == '__main__':
    unittest.main()
