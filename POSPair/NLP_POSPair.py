#Importing Stanford libraries
from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')

class NLP:
    
    def __pos(annotatedObject, word):
        #fetching part-of-speech of specific word from annotated parsed sentence (Further on using pos = part-of-speech)
        try:
            i = 0
            while True:
                #Finding pos of word from annotated object
                if(annotatedObject['sentences'][0]['tokens'][i]['originalText'] == word): 
                    partOfSpeech = annotatedObject['sentences'][0]['tokens'][i]['pos']
                    break
                else:
                    i = i + 1     
                
            #pos notations #Converting it into 8 major part-of-speech           
            noun = ['NN', 'NNS', 'NNP', 'NNPS', 'POS']
            pronoun = ['PRP', 'PRP$', 'WP', 'WP$']
            adjective = ['JJ', 'JJR', 'JJS', 'CD', 'DT', 'EX', 'FW', 'LS', 'PDT', 'RP', 'WDT']                
            verb = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'MD']
            adverb = ['RB', 'RBR', 'RBS', 'WRB']
            preposition = ['IN', 'TO']
            conjunction = ['CC']
            interjection = ['UH']
            others = ['SYM']
        
            if(partOfSpeech in noun):
                return 'Noun'
            if(partOfSpeech in pronoun):
                return 'Pronoun'
            if(partOfSpeech in adjective):
                return 'Adjective'
            if(partOfSpeech in verb):
                return 'Verb'
            if(partOfSpeech in adverb):
                return 'Adverb'
            if(partOfSpeech in preposition):
                return 'Preposition'
            if(partOfSpeech in conjunction):
                return 'Conjunction'
            if(partOfSpeech in interjection):
                return 'Interjection'
            if(partOfSpeech in others):
                return 'null'
            if not partOfSpeech: #if pos is blank or error
                return 'null'
        except:
            print("Error finding part-of-speech of given word. Word may not belong to the Annotated Object")
            return None

    def __findPairingWord(annotatedObject, dependantWord, text):
        #Fetching pairing word of the dependant word and check if it matches pos relation
        try:
            #Parsing through annotated sentence to find governor word
            for i in range(len(text)):
                if(annotatedObject['sentences'][0]['basicDependencies'][i]['dependentGloss'] == dependantWord):
                    governerWord = annotatedObject['sentences'][0]['basicDependencies'][i]['governorGloss']
                    break
            
            notations = [",",".","?",";",":","<",">","/","'",'"','!','&']
            #Return None, if governer equals to ROOT or contains notations
            if (governerWord == 'ROOT' or governerWord in notations):
                return None

            dependantWordPos = NLP.__pos(annotatedObject, dependantWord)
            governerWordPos = NLP.__pos(annotatedObject, governerWord)

            #According to relation between words based on part-of-speech semantic understanding, validating word pair
            if(dependantWordPos == 'Noun'):
                if(governerWordPos == 'Adjective' or 'Verb' or 'Pronoun' or 'Noun' or 'Conjunction' or 'Preposition'):
                    return governerWord
        
            if(dependantWordPos == 'Adjective'):
                if(governerWordPos == 'Noun' or 'Adverb' or 'Pronoun'):
                    return governerWord
        
            if(dependantWordPos == 'Verb'):
                if(governerWordPos == 'Adverb' or 'Noun' or 'Pronoun'):
                    return governerWord
        
            if(dependantWordPos == 'Adverb'):
                if(governerWordPos == 'Adjective' or 'Verb' or 'Adverb'):
                    return governerWord
          
            if(dependantWordPos == 'Preposition'):
                if(governerWordPos == 'Noun'):
                    return governerWord
                
            if(dependantWordPos == 'Conjunction'):
                if(governerWordPos == 'Noun'):
                    return governerWord
                
            if(dependantWordPos == 'Pronoun'):
                if(governerWordPos == 'Adjective' or 'Verb' or 'Noun' or 'Pronoun' or 'Conjunction' or 'Preposition'): 
                    return governerWord
            else:
                #If not related, pass governor as dependant in same function, iterate the loop, fetch it's governor word and validate if relation exists
                NLP.__findPairingWord(annotatedObject, governerWord, text)
            
        except:
            print("Error while fetching pairing word")
            print("Sentence - " + text)
            return None

    def __createWordPairWithValues(text):
        #Creating Word pairs with values #Text should be just one sentence
        try:
            #Parsing Text
            annotatedObject = nlp.annotate(text, properties = {
            'annotators' : 'parse,pos,tokenize,ssplit',
            'outputFormat' : 'json'
            })
            
            tokens = NLP.__SentenceIntoWords(text)
            wordPairObjects = []
            
            #Fetching word pairs
            wordPairs = NLP.__createWordPairs(text)
            
            #Iterating through each word pair to create objects
            for pair in wordPairs:
                contextPairs = []
                words = NLP.separateWordValue(pair)
                partOfSpeechOfWord = NLP.__pos(annotatedObject, words[0])
                partOfSpeechOfValue = NLP.__pos(annotatedObject, words[1])
                contextPairs.extend(wordPairs)
                context = NLP.__backgroundValues(contextPairs, pair)
                   
                wordPairObjects.append(NLP.Word(words[0], words[1], partOfSpeechOfWord, partOfSpeechOfValue, text, context, tokens))
            return wordPairObjects
        except Exception as ex:
            if(str(ex.args) == "('list index out of range',)"):
                return wordPairObjects
            print("Error in sentence parsing OR Word not present in sentence parsed")
            print("Sentence - " + text)
            return None
        
    def __createWordPairs(text):
        #Creating Word pairs #Text should be just one sentence
        try:
            #Parsing text
            annotatedObject = nlp.annotate(text, properties = {
            'annotators' : 'tokenize,pos,ssplit,parse',
            'outputFormat' : 'json'
            })
           
            notations = [",",".","?",";",":","<",">","/","'",'"']
            wordPairs = []
            #Parsing through whole sentence & fetching relation between words
            for i in range(len(text)):
                dependantWord = annotatedObject['sentences'][0]['basicDependencies'][i]['dependentGloss']
                if (dependantWord in notations):
                    continue
                #Fetching governor word of the dependant word
                governorWord = NLP.__findPairingWord(annotatedObject,dependantWord, text)
                if(governorWord == None):
                    continue
                #Organizing the word pair according to pos word relations
                syntacticParsed = NLP.__POSWordRelation(annotatedObject, dependantWord + " " + governorWord)
                
                wordPairs.append(syntacticParsed)
            return wordPairs
        except Exception as ex:
            if(str(ex.args) == "('list index out of range',)"):
                return wordPairs
            print("Error in sentence parsing OR Word may not be present in sentence parsed")
            print("Sentence - " + text)
            return None

    class Word(object):
        word = ""
        value = ""
        posOfWord = ""
        posOfValue = ""
        sentence = ""
        context = ""
        tokens = ""

        def __init__(self, word, value, posOfWord, posOfValue, sentence, context, tokens):
            self.word = word
            self.value = value
            self.posOfWord = posOfWord
            self.posOfValue = posOfValue
            self.sentence = sentence
            self.context = context
            self.tokens = tokens

        def ObjectCreate(word, value, posOfWord, posOfValue, sentence, context, tokens):
            createdObject = Word(word, value, posOfWord, posOfValue, sentence, context, tokens)
            return createdObject

    def __subjectNoun(text):
        #Returns subject noun
        annotatedObject = nlp.annotate(text, properties = {
            'annotators' : 'parse,pos,tokenize,ssplit',
            'outputFormat' : 'json'
        })
        i = 0
        try:
            for j in text: #return subject noun from first sentence
                if(annotatedObject['sentences'][0]['basicDependencies'][i]['dep'] == "nsubj"):
                    return annotatedObject['sentences'][0]['basicDependencies'][i]['dependentGloss'] #if no subject noun, it will return null
                i += 1
        except:
            return None

    def __backgroundValues(contextPairs, pair):
        #Fetching context of each pair
        try:
            #Removing pair & return rest of the pairs
            contextPairs.remove(pair) 
            return contextPairs
        except:
            print("Error while fetching context values-" + text)
            return None

    def separateWordValue(text):
        #Separating words from word pair and storing in list
        try:
            WordValues = str(text).split()
            return WordValues
        except:
            print("Error while seperating word values of pair -" + text)
            return None

    def __POSWordRelation(annotatedObject, text):
        #Text as word-value pair
        #Organizing words in word pair as per part-of-speech semantics
        try:
            #Seperating word pair
            words = NLP.separateWordValue(text)
            posWord1 = NLP.__pos(annotatedObject, words[0])
            posWord2 = NLP.__pos(annotatedObject, words[1])

            #Organizing words
            if(posWord1 == 'Noun'):
                if(posWord2 == 'Adjective' or 'Verb' or 'Pronoun' or 'Noun' or 'Conjunction' or 'Preposition'):
                    parsedPair = (words[0] + ' ' + words[1])
                return parsedPair

            if(posWord1 == 'Adjective'):
                if(posWord2 == 'Noun' or 'Pronoun'):
                    parsedPair = (words[1] + ' ' + words[0])
                if(posWord2 == 'Adverb'):
                    parsedPair = (words[0] + ' ' + words[1])
                return parsedPair

            if(posWord1 == 'Verb'):
                if(posWord2 == 'Adverb'):
                    parsedPair = (words[0] + ' ' + words[1])
                if(posWord2 == 'Noun' or 'Pronoun'):
                    parsedPair = (words[1] + ' ' + words[0])
                return parsedPair

            if(posWord1 == 'Adverb'):
                if(posWord2 == 'Adverb'):
                    parsedPair = (words[0] + ' ' + words[1])
                if(posWord2 == 'Verb' or 'Adjective'):
                    parsedPair = (words[1] + ' ' + words[0])
                return parsedPair
          
            if(posWord1 == 'Preposition'):
                if(posWord2 == 'Noun'):
                    parsedPair = (words[1] + ' ' + words[0])
                return parsedPair
                
            if(posWord1 == 'Conjunction'):
                if(posWord2 == 'Noun'):
                    parsedPair = (words[1] + ' ' + words[0])
                return parsedPair
                   
            if(posWord1 == 'Pronoun'):
                if(posWord2 == 'Adjective' or 'Verb' or 'Noun' or 'Pronoun' or 'Conjunction' or 'Preposition'):
                    parsedPair = (words[0] + ' ' + words[1])
                return parsedPair
        except:
            print("Error while structuring POS relation -" + text)        
            return None

    def __TextIntoSentences(text):
        #Converting text into sentences
        try:
            annotatedObject = nlp.annotate(text, properties = {
            'annotators' : 'tokenize,parse,pos,depparse',
            'outputFormat' : 'json'
            })
            sentences = []
            
            #Iterating through annotated object to create sentences
            for i in range(len(text)):
                sentence = " ".join(t["word"] for t in annotatedObject['sentences'][i]["tokens"])  
                sentences.append(sentence)
            return sentences
        except Exception as ex:
            if(str(ex.args) == "('list index out of range',)"):
                return sentences
            print("Error while annotating sentence - " + text)
            return None

    def __SentenceIntoWords(text):
        #Converting into words
        try:
            annotatedObject = nlp.annotate(text, properties = {
            'annotators' : 'tokenize,parse,pos,depparse',
            'outputFormat' : 'json'
            })
            Words = []
            
            #Iterating through annotated object to create list of words
            for i in range(len(text)):
                Words.append(annotatedObject['sentences'][0]['tokens'][i]['originalText'])  
            return Words
        except Exception as ex:
            if(str(ex.args) == "('list index out of range',)"):
                return Words
            print("Error while converting sentence into list of words - " + text)
            return None

    def WordPairs(text):
        #Returns word pairs
        try:
            #Validating input
            if(NLP.__inputValidation(text) == True):
                #Converting text into sentences
                sentences = NLP.__TextIntoSentences(text)
                wordPairs = []
                #Iterating through each sentence
                for sentence in sentences:
                    wordPairs.append(NLP.__createWordPairs(sentence))
                return wordPairs
        except Exception as ex:
            if(str(ex.args) == "('Input is empty',)" or "('Only 500 characters allowed',)"):
                return None
            print(str(ex.args))
            return None

    def WordPairsWithValues(text):
        #Returns word pair with associated values
        try:
            #Validating input
            if(NLP.__inputValidation(text) == True):
                #Converting text into sentences
                sentences = NLP.__TextIntoSentences(text)
                wordPairs = []
                #Iterating through each sentence
                for sentence in sentences:
                    wordPairs.append(NLP.__createWordPairWithValues(sentence))
                return wordPairs
        except Exception as ex:
            if(str(ex.args) == "('Input is empty',)" or "('Only 500 characters allowed',)"):
                return None
            print(str(ex.args))
            return None

    def __inputValidation(text):
        #Validating input
        #Checking if text is empty
        if not text:
            print("Input is empty")
            raise ValueError("Input is empty")
        else:
            #Checking if input is string or integer
            if(type(text) == str or type(text) == int):
                #Checking input length is under limit
                if(len(text) > 500):
                    print ("Error! Only 500 characters allowed.")
                    raise ValueError("Only 500 characters allowed")
                else:
                    return True
            else:
                print("Input is not string")
                return None
