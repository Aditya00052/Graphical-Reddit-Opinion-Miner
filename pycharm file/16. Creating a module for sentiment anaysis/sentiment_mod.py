import random
import pickle
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


documents_f = open("docs/documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()


word_features5k_f = open("docs/word_features5k.pickle", "rb")
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()


def find_features(review):
    words = word_tokenize(review)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)


testing_set = featuresets[10000:]
training_set = featuresets[:10000]


open_file = open("pickled models/naivebayes.pickle", "rb")
classifier = pickle.load(open_file)
open_file.close()

open_file = open("pickled models/MultinomialNB.pickle", "rb")
MNB_classifier = pickle.load(open_file)
open_file.close()


open_file = open("pickled models/BernoulliNB.pickle", "rb")
BernoulliNB_classifier = pickle.load(open_file)
open_file.close()

open_file = open("pickled models/LogisticRegression.pickle", "rb")
LogisticRegression_classifier = pickle.load(open_file)
open_file.close()

open_file = open("pickled models/LinearSVC.pickle", "rb")
LinearSVC_classifier = pickle.load(open_file)
open_file.close()

open_file = open("pickled models/SGDClassifier.pickle", "rb")
SGDC_classifier = pickle.load(open_file)
open_file.close()



voted_classifier = VoteClassifier(
                                  classifier,
                                  LinearSVC_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier)


def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)
