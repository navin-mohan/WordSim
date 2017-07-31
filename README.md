# WordSim
A simple Python wrapper for the [**GloVe**](https://nlp.stanford.edu/projects/glove/) pretrained word vectors.
Easy functions for [**Cosine Similarity**](https://en.wikipedia.org/wiki/Cosine_similarity) and [**Euclidian Distance**](https://en.wikipedia.org/wiki/Euclidean_distance).

## How to Install (using pip)

```bash
pip install git+git://github.com/nvnmo/WordSim.git
```

## Usage

```python
from wordsim import WordSim

# path to the pretrained GloVe word vectors
GLOVE_FILE_NAME = './glove.6B.50d.txt'

# loading the vectors at creation
w = WordSim(GLOVE_FILE_NAME)

# you can also do this
w = WordSim()
w.load_glove_model(GLOVE_FILE_NAME)

cosine_similarity = w.similarity("girl","woman")
euclidian_distance = w.distance("girl","woman")

# do something with the values..

print("Cosine Similarity: {0} Euclidian Distance: {1}".format(cosine_similarity,euclidian_distance))
    
```

## Where to find GloVe pretrained models?

You can find them [here](https://github.com/stanfordnlp/GloVe).

### Doesn't fit your needs?

Checkout this [repo](https://github.com/maciejkula/glove-python).

