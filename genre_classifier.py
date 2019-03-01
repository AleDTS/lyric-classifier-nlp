import pandas as pd
import glob, os, string, nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
from joblib import dump, load

nltk.download(info_or_id='stopwords')

from nltk.corpus import stopwords

class GenreClassifier(object):

	# Method to remove stopwords from text and returns a list of words
	def text_clean(self, mess):
	    nopunc = [c for c in mess if c not in string.punctuation]
	    nopunc = ''.join(nopunc)
	    return [w for w in nopunc.split() if w.lower() not in stopwords.words('portuguese')]

	# Method to predict from model
	def predict(self,lyric):
		return self.pipeline.predict(lyric)[0]

	# Method to train the data
	def train(self, data_dir='./lyrics/', test=False, dump=True):	
		# Read csv file and concatenate them in one pandas DataFrame object
		lyrics = pd.concat([pd.read_csv(f).assign(genre=os.path.basename(f).split(".")[0]) for f in glob.glob(data_dir+"*.csv")])

		# If method argument test = True, gives model evaluation
		if test == True:
			lyric_train, lyric_test, genre_train, genre_test = train_test_split(lyrics['lyric'], lyrics['genre'], test_size=0.2)

			self.pipeline.fit(lyric_train, genre_train)
			predictions = self.pipeline.predict(lyric_test)
			print(classification_report(predictions, genre_test))
		# Default: trains model with all given data
		else:
			self.pipeline.fit(lyrics['lyric'], lyrics['genre'])

		# Save trained model to file
		if dump==True:
			self.dump_model()
	
	# Method to dump model into file
	def dump_model(self):
		dump(self.pipeline, 'model.joblib')

	# Method to load model from file
	def load_model(self):
		return load('model.joblib')

	def __init__(self):
		super(GenreClassifier, self).__init__()		

		# Define model`s pipeline
		self.pipeline = Pipeline([
		    ('bow', CountVectorizer(analyzer=self.text_clean)),	#Bag of words, containing words and it`s frequency
		    ('tfidf', TfidfTransformer()),						#TF-IDF: weight to define words importances
		    ('classifier', MultinomialNB())						#Naive Bayes classification algorithm
		])