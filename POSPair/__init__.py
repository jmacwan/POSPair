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

def POSPairWordEmbeddings(sentences=None, size=100, alpha=0.025,
                 max_vocab_size=None, sample=1e-3, seed=1, workers=3, min_alpha=0.0001,
                 sg=1, hs=0, negative=5, ns_exponent=0.75, cbow_mean=1, hashfxn=hash, iter=5, null_word=0,
                 trim_rule=None, sorted_vocab=1, batch_words=10000, compute_loss=False, callbacks=(),
                 max_final_vocab=None):
    try:
        return NLP_POSPair.WordRepresentations.POSPairWordEmbeddings(sentences=sentences, size=size, alpha=alpha,
                 max_vocab_size=max_vocab_size, sample=sample, seed=seed, workers=workers, min_alpha=min_alpha,
                 sg=sg, hs=hs, negative=negative, ns_exponent=ns_exponent, cbow_mean=cbow_mean, hashfxn=hashfxn, iter=iter, null_word=null_word,
                 trim_rule=trim_rule, sorted_vocab=sorted_vocab, batch_words=batch_words, compute_loss=compute_loss, callbacks=callbacks,
                 max_final_vocab=max_final_vocab)
    except:
        return None

def txtFileInput(fileName, size=100, alpha=0.025,
                 max_vocab_size=None, sample=1e-3, seed=1, workers=3, min_alpha=0.0001,
                 sg=1, hs=0, negative=5, ns_exponent=0.75, cbow_mean=1, hashfxn=hash, iter=5, null_word=0,
                 trim_rule=None, sorted_vocab=1, batch_words=10000, compute_loss=False, callbacks=(),
                 max_final_vocab=None):
    try:
        return NLP_POSPair.WordRepresentations.txtFileInput(fileName, size=size, alpha=alpha,
                 max_vocab_size=max_vocab_size, sample=sample, seed=seed, workers=workers, min_alpha=min_alpha,
                 sg=sg, hs=hs, negative=negative, ns_exponent=ns_exponent, cbow_mean=cbow_mean, hashfxn=hashfxn, iter=iter, null_word=null_word,
                 trim_rule=trim_rule, sorted_vocab=sorted_vocab, batch_words=batch_words, compute_loss=compute_loss, callbacks=callbacks,
                 max_final_vocab=max_final_vocab)
    except:
        return None
