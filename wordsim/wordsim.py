import numpy as np



class WordSim:
    '''
     Wrapper for pretrained GloVe word vectors. Provides simple 
     functions for computing cosine similarity and euclidian distance
     between words.
    '''

    def __init__(self, filename=None):
        self.model = None


        # initialize with glove model form filename
        if not filename is None:
            self.load_glove_model(filename)



    def load_glove_model(self, filename,verbose=False):
        '''Loads the globe vector embeddings'''
        if verbose:
            print("Loading Glove Model...")
        self.model = dict()
        count = 0
        with open(filename, 'r') as f:
            for line in f:
                splitline = line.split()
                word = splitline[0]
                embedding = np.array([float(val) for val in splitline[1:]], dtype=float)
                self.model[word] = embedding
                count += 1
        if verbose:
            print("Done loading the model! {count} entries loaded.".format(count=count))
        
    def similarity(self, word1, word2):
        '''returns the cosine similarity of the two words(preprocessed) if they exist in the corpus'''    
        word1, word2 = self.get_word_vectors(word1, word2)

        if all((word1 is not None, word2 is not None)):
            return np.dot(word1, word2)/(np.linalg.norm(word1)*np.linalg.norm(word2)) # cosine similarity
        else:
            return 0 # not in corpus

    def distance(self, word1, word2):
        '''computes the euclidian distance between the words word1 ans word2'''

        word1, word2 = self.get_word_vectors(word1, word2)

        if all((word1 is not None, word2 is not None)):
            return np.linalg.norm(word1-word2) # euclidian distance
        else:
            return None # not in corpus
        



    def get_word_vectors(self,*args):
        '''returns the vectors corresponding to the words'''

        try:
            assert self.model is not None # model must be loaded before this
        except AssertionError as err:
            print("Model not found. Make sure that the glove model is loaded")
        vectors = []

        for word in args:
            try:
                if not isinstance(word,str): 
                    raise ValueError("Only Strings can be converted to vectors")
                vectors.append(self.model.get(word,None))
            except ValueError as err:
                print("Error Converting word to vector: " + repr(err) )



        vectors = self.preprocess_words(*vectors)

        return vectors
                
    

    def preprocess_words(self,*args):
        '''Strips the words and converts them to lowercase'''
        return ( arg.strip().lower() for arg in args if arg )
