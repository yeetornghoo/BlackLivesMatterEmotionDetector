# Social Movement Sentiment

## Lexicon Libraries
Following Libraries are being used to compare the accuracy of the lexicon on the sample tweets.

### NRC
URL: https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm
Lexicon Use: NRC-Emotion-Intensity-Lexicon-v1/OneFilePerEmotion/* (All individual mood files)
Mood Class: anger, anticipation, disgust, fear, joy, sadness, surprise, trust

### Depeche Mood ++
URL: https://github.com/marcoguerini/DepecheMood/tree/master/DepecheMood%2B%2B
Lexicon Use: DepecheMood++/DepecheMood_english_token_full.tsv
Mood Class: afraid, amused, angry, annoyed, dontcare, happy, inspired, sad

### ECO SenticNet Mood
URL: https://sentic.net/downloads/
Lexicon Use: emosenticnet.csv
Mood Class: anger, disgust, fear, joy, sadness, surprise']

---

# Experiment on #BlackLivesMetter Tweets
The sample test tweets are located in each folder under /dataset. For example the tweets about the #BlackLivesMetter is located in /dataset/blm_minesota. This dataset are the tweets downloaded (by using this python code https://github.com/yeetornghoo/PythonTweetDownload) with conditions
- Date between 2020-05-15 and 2020-07-15 
- Tweet retweet count and tweet favorites count more than 20

## Data Cleaning
Python file: /dataset/blm_minesota/0_process.py

Following are the data cleaning tasks
- Remove Unwanted Attributes
- Clone the original tweet text "text" (treat as backup) to additional attribute "tweet_text" (Cleaning done on this attribute)
- Step 1: Detected Tweet Language on "tweet_text"
    - Use google translate to detect the langague of the tweets. remove all none english tweets.
    - Saved outcome /dataset/blm_minesota/01-post-translate-dataset.csv
- Step 2: Replace word and Spelling Error Correction on "tweet_text"
    - Replace word. For example *He's* to *He is*, *Don't* to *Do not*
    - Remove @USERNAME
    - Remove # and Split Hashtag by Upper Case (e.g. "ILoveYou" to "I Love You")
    - Replace Emoji to String
    - Saved outcome /dataset/blm_minesota/02-post-cleaning-dataset.csv
- Step 3:
    - Tokenized "tweet_text"
    - Correct Spelling Error (Correction Word File /dataset/_custome/correction.csv)
    - Tokenized and Lemmatized on "tweet_text" and saved to "lemma_tweet_text"
    - Saved outcome /dataset/blm_minesota/03-post-nlp-dataset.csv

by end of the steps above, the dataframe will have
- "text": Original Tweet
- "tweet_text": Tokenized Cleaned Tweets
- "lemma_tweet_text": Tokenized Cleaned, Lemmataized Tweets

## Sentiment Labelling
Python file: /dataset/blm_minesota/1_label_sentiment.py

- By default (is_standard_model: False), the python code will use the lexicon libraries above to label te tweets accordingly, the output of this python code 04-post-sentiment-dataset.csv will provide a csv with the mood class for each of the lexicon library.  
- *Each of tweets will combine the normal form of the words and Lemmatized word, then get the unique words only from the sentence. *

### NRC Lexicon
- NRC Lexicon library provide corpus in 8 file (one mood per file) and each mood will have the word and the intensity score. 
- Steps
    1. Get Unique words (Combined Standard and Lemmatized Form) 
    2. For-Loop Each Sentence and then For-Loop the words
    3. Find the Tweet' Word on each Mood Lexicon File and Extract the Score
    4. Count the number of time the words appear and sum the score
    5. The mood with higher score will be the final mood for that sentence
    6. Added 3 new attribute 
        - nrc_sentiment : Highest Score Mood Name
        - nrc_sentiment_count: Highest Score Mood Count
        - nrc_sentiment_score: Highest Score Mood Score
    7. Save the file to /dataset/blm_minesota/tmp/nrc-processed_dataset.csv
- Limitation
    - TBC

### Depeche Mood ++ Lexicon
- Depeche Mood library provide only 1 files, inside the file with following content the words and the intensity for each mood (AFRAID, AMUSED, ANGRY, ANNOYED, DONT_CARE, HAPPY, INSPIRED, SAD, freq)
- Steps
    1. Get Unique words (Combined Standard and Lemmatized Form) 
    2. For-Loop Each Sentence and then For-Loop the words
    3. Find the Tweet' Word on the Mood Lexicon File and Extract the Score/Intensity
    4. Count the number of time the words appear and sum the score
    5. The mood with higher score will be the final mood for that sentence
    6. Added 3 new attribute 
        - dpm_sentiment : Highest Score Mood Name
        - dpm_sentiment_count: Highest Score Mood Count
        - dpm_sentiment_score: Highest Score Mood Score
    7. Save the file to /dataset/blm_minesota/tmp/dpm-processed_dataset.csv
- Limitation
    - The Corpus was build by using the text from website in Philippenes, some words in the corpus are not english
    
### EmoSenticNet Lexicon
- EmoSenticNet provide only 1 files, inside the file with following content the words and 1 (yes) or 0 (no) for the mood (Anger, Disgust, Joy, Sad, Surprise, Fear). 
- Steps
    1. Get Unique words (Combined Standard and Lemmatized Form) 
    2. For-Loop Each Sentence and then For-Loop the words
    3. Find the Tweet' Word on the Mood Lexicon File and Extract 1/0. 
    4. Sum the mood count. *If the sentence have more than 1 mood with same highest count. the Tweet will not be labelled any mood*
    5. Higher mood count will be the final mood for that sentence
    6. Added 3 new attribute 
        - esn_sentiment : Highest Score Mood Name
        - esn_sentiment_count: Highest Score Mood Count
        - esn_sentiment_score: Highest Score Mood Score
    7. Save the file to /dataset/blm_minesota/tmp/esn-processed_dataset.csv
- Limitation
    - A lot of "joy" word, end up most of the tweets are labelled as "Joy"
    - it is because this lexicon has no intensity / score, where can only use the number of word to determine the mood. However some cases the tweet have same count for more than one mood.     
    

Due to each of the lexicon library will have own set of mood, it is a bit difficult to compare. According to F. S. Tabak et al [1]. The mood class can be merged into a single set in order to compare. You can set (is_standard_model: True) and it will merge the mood into one set for all library

# Reference
[1] F. S. Tabak and V. Evrim, "Comparison of emotion lexicons," 2016 HONET-ICT, Nicosia, 2016, pp. 154-158, doi: 10.1109/HONET.2016.7753440. https://ieeexplore.ieee.org/document/7753440