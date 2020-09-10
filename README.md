# Social Movement Sentiment

## Lexicon Libraries
Following Libraries are being used to compare the accuracy of the lexicon on the sample tweets.

### NRC
URL: https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm
Lexicon Use: NRC-Emotion-Intensity-Lexicon-v1/OneFilePerEmotion/* (All individual mood files)

### Depeche Mood ++
URL: https://github.com/marcoguerini/DepecheMood/tree/master/DepecheMood%2B%2B
Lexicon Use: DepecheMood++/DepecheMood_english_token_full.tsv

### ECO SenticNet Mood
URL: https://sentic.net/downloads/
Lexicon Use: emosenticnet.csv

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
    - Correct Spelling Error (Correction Word File /dataset/_custome/correction.csv)
    - Saved outcome /dataset/blm_minesota/02-post-cleaning-dataset.csv
- Step 3:
    - Tokenized "tweet_text"
    - Tokenized and Lemmatized on "tweet_text" and saved to "lemma_tweet_text"
    - Saved outcome /dataset/blm_minesota/03-post-nlp-dataset.csv

by end of the steps above, the dataframe will have
- "text": Original Tweet
- "tweet_text": Tokenized Cleaned Tweets
- "lemma_tweet_text": Tokenized Cleaned, Lemmataized Tweets

## Sentiment Labelling
