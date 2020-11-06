from Controller import GitController

exec(open('script_1_process.py').read())
exec(open('script_2_label_sentiment.py').read())
exec(open('script_3_analysis_lexicon.py').read())
exec(open('script_4_generate_training_dataset.py').read())

# COMMIT TO GIT
GitController.commit("auto: update blm_baltimore")