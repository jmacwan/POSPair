import POSPair.NLP_POSPair

def WordPairs(text):
    try:
        return NLP_POSPair.NLP.WordPairs(text)
    except:
        return None

def WordPairsWithValues(text):
    try:
        return NLP_POSPair.NLP.WordPairsWithValues(text)
    except:
        return None

def separateWordPair(text):
    try:
        return NLP_POSPair.NLP.separateWordValue(text)
    except:
        return None