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
https://github.com/yeetornghoo/SocialMovementSentiment/wiki/Data-Cleaning

## Sentiment Labelling
https://github.com/yeetornghoo/SocialMovementSentiment/wiki/Fine-Gain-Sentiment-Classification-By-Lexicon