# Practice using sci-kit learn
# from blog http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/

# define set of example documents:
documents = (
"The sky is blue",
"The sun is bright",
"The sun in the sky is bright",
"We can see the shining sun, the bright sun"
)

# instantiate the skleanr TF-IDF vectorizer
# and transform documents into the TF-IDF matrix

