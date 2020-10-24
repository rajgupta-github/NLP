# Natural Language Processing


**Pre-processing**
- Tokenization and Lowercase
- Stemming and Lemmatization
- Stopwords Removal

**Embeddings (Words->Vectors)**
- Frequency Based
   - Bag of Words (No order of words)
   - TF-IDF (Normalized frequency = (No of times of w in D1 / No of Unique Words in D1) * log(No of Documents /No of times w in present in all documents + 1)
- Prediction Based
   - Word2Vec 
        - CBOW (Continuous Bag of Words)
        - SG (Skip Gram)
        -  [http://jalammar.github.io/illustrated-word2vec/], 
           [https://kavita-ganesan.com/comparison-between-cbow-skipgram-subword/#.X4EnWJMzZQ1]
           [https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html#sphx-glr-auto-examples-tutorials-run-word2vec-py]
  - Glove
  - Fast Text
- Repository of Word Embeddings [http://vectors.nlpl.eu/repository/]
- Visualization [https://projector.tensorflow.org/] [https://dash-gallery.plotly.host/dash-word-arithmetic/] 
         

**Basics**
- RNN
![RNN](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-unrolled.png)
   - Parameter Sharing Concept (The main purpose of parameter sharing is a reduction of the parameters that the model has to learn)
   - [https://stats.stackexchange.com/questions/221513/why-are-the-weights-of-rnn-lstm-networks-shared-across-time] [https://stackoverflow.com/questions/47865034/recurrent-nns-whats-the-point-of-parameter-sharing-doesnt-padding-do-the-tri#:~:text=The%20main%20purpose%20of%20parameter,purpose%20of%20using%20a%20RNN.&text=This%20drastically%20reduces%20the%20number,patterns%20at%20different%20time%20steps.]
   - Vanishing/Exploding Gradient Problem -> Loss of Long Term Context
- LSTM
   - [https://colah.github.io/posts/2015-08-Understanding-LSTMs/]
- GRU
- Encoder-Decoder
- Transformer (6 layers of Encoder and Decoder with Self Attention on encoder side and attention at decoder side)

**Transformer Based Models**
[https://github.com/huggingface/transformers]
- BERT [https://huggingface.co/transformers/model_doc/bert.html]
   - Encoder stack of transformer architecture
   - Performs multiple NLP Tasks [http://jalammar.github.io/illustrated-bert/]
         - SPAM/Sentence Classification
         - Image Captioning
         - Word Embedding Generation 
   - BERTBASE (110M parameters, 12 layers in Encoder Stack, 768 hidden units in FF neural network)
   - BERTLARGE (340M parameters, 24 layers in Encoder Stack, 1024 hidden units in FF neural network)

**NLP Taks**
- Sentiment Analysis
- Language/Machine translation
- Question and Answering
- Abstrative and Extractive Text Summarization
- Named Entity Recognition(NER)
- Sentence Completion
- Topic Modeling
- Text Classification
- Language Modeling
- PartOfSpeech Taging(POS) [https://sites.google.com/site/partofspeechhelp/]
- Image Captioning


**Libraries used for NLP**
- NLTK
- Spacy
- Gensim for Topic Modeling
- Stanford NLP (Latest replaced with Stanza – A Python NLP Package for Many Human Languages)
- Textblob for sentiment analysis
- Scikit Learn for CountVectorizer, TFIDFVectorizer, ML
- Inflect (converting numbers to words)



**Resources**
- Krish Naik NLP Playlist
 - https://www.youtube.com/watch?v=6ZVf1jnEKGI&list=PLZoTAELRMXVMdJ5sqbCK2LiM0HhQVWNzm
- Krish Naik Deep Learning Playlist
 - https://www.youtube.com/playlist?list=PLZoTAELRMXVPGU70ZGsckrMdr0FteeRUi
- Automatic Question Answering from FAQs 
 - https://www.youtube.com/watch?v=ZxR38An5TQE
 - https://github.com/lavanyats/QuestionAnswering_From_FAQ_Tutorial
- Natural Language Processing in Python
 - https://www.youtube.com/watch?v=xvqsFTUsOmc
 - https://naspers.udemy.com/course/nlp-natural-language-processing-with-python/learn/lecture/13241158?start=0#overview
- http://jalammar.github.io/illustrated-transformer/ 
- Code Emporium Youtube channel
 - https://www.youtube.com/channel/UC5_6ZD6s8klmMu9TXEB_1IA
- Tensorflow Lite for NLOP
 - https://blog.tensorflow.org/2020/09/whats-new-in-tensorflow-lite-for-nlp.html
- MLU NLP
 - https://www.youtube.com/playlist?list=PL8P_Z6C4GcuWfAq8Pt6PBYlck4OprHXsw
- NLP Word2Vec
 - https://towardsdatascience.com/nlp-101-word2vec-skip-gram-and-cbow-93512ee24314#:~:text=In%20the%20CBOW%20model%2C%20the,used%20to%20predict%20the%20context%20
- https://iksinc.online/tag/continuous-bag-of-words-cbow/
- https://www.machinelearningplus.com/nlp/cosine-similarity/
- https://inblog.in/A-gentle-Introduction-to-LSTM-1DydP2G9fP
- https://inblog.in/Neural-Machine-Translation-A-beginning-of-Attention-j8CNM8hjWX
- https://www.youtube.com/playlist?list=PLwFaZuSL_mfpqO25zyIdTCRCr6Mo4xqHE (SPACY PLAYLIST)
