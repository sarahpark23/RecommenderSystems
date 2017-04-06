# Practice using sci-kit learn
# from blog http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/

# define set of example documents:
documents = (
"The sky is blue",
"The sun is bright",
"The sun in the sky is bright",
"We can see the shining sun, the bright sun"
)

print "Documents: {}".format(documents)

# instantiate the skleanr TF-IDF vectorizer
# and transform the documents into the TF-IDF matrix

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print "tfidf_matrix.shape, {}".format(tfidf_matrix.shape)

# calculation of cosine similirity between the first document
# ("The sky is blue") with each of the other documents of the set:
from sklearn.metrics.pairwise import cosine_similarity
cossim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
print "Cosine similarity: {}".format(cossim)

# Calculatino of the angle between the first and the third documents:
import math
angle_in_radians = math.acos(cossim[0,2])

print "Angle in radians between first doc and third doc: {}".format(angle_in_radians)
print "Angle in degrees between first doc and third doc: {}".format(math.degrees(angle_in_radians))