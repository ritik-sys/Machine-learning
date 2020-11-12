#!/usr/bin/env python
# coding: utf-8

# # Movie Rating Prediction from Reviews

# In[3]:


from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


# In[5]:


#initialize objects
# r'\w+' is for extracting all the words
tokenizer = RegexpTokenizer(r'\w+')
stopwords = set(stopwords.words('english'))
ps = PorterStemmer()


# # This function will do the-
# - tokenization
# - stopword removal
# - stemming

# In[60]:


def getCleanReview(review):
    review = review.lower()
    review = review.replace("<br /><br />"," ")
    
    #tokenize
    tokens = tokenizer.tokenize(review)
    #remove stopwords
    new_tokens = [token for token in tokens if token not in stopwords]
    #stemming
    stemmed = [ps.stem(token) for token in new_tokens]
    #join list of words to form a sentence
    cleaned_review = " ".join(stemmed)
    
    return cleaned_review
    


# ##### let us test our function by passing a sampe review

# In[61]:


sample = "I loved this movie since I was 7 and I saw it on the opening day. It was so touching and beautiful. I strongly recommend seeing for all. It's a movie to watch with your family by far.<br /><br />My MPAA rating: PG-13 for thematic elements, prolonged scenes of disastor, nudity/sexuality and some language."
getCleanReview(sample)


# # Handling files to read reviews

# In[58]:


def getStemmedDocument(inputFile,outputFile):
    #making objects for writing and reading of output and input file
    outFile = open(outputFile,"w")
    inFile = open(inputFile,"r")
    #reading all lines from input file
    lines = inFile.readlines()
    #writing line by line in output file
    for line in lines:
        cleaned_review = getCleanReview(line)
        print((cleaned_review),file=outFile)
    outFile.close()


# In[59]:


getStemmedDocument("./IMDB/imdb_small_trainX.txt","./IMDB/imdb_small_cleaned_trainX.txt")


# # We will export this as a module and will use this in other files to getCleanedData
