from Controller import FileController, LogController
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn import svm
from numpy import mean
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import RepeatedKFold
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from Helper import FolderHelper

confusion_matrix_file_name_pattern = "{}_{}_confusion_matrix.png"

def confusion_matrix(classifier, X, y, name, wordvectorname, df, path_dir):
    class_names = df.sentiment.unique()

    fig, ax = plt.subplots(figsize=(8, 6))

    disp = plot_confusion_matrix(classifier, X, y, cmap=plt.cm.Blues, ax=ax)

    plt.xticks(rotation=50)

    plt.title("Confusion matrix of {} {}".format(wordvectorname, name))
    ax.tick_params(axis='both', which='major', labelsize=10)
    img_file_name = confusion_matrix_file_name_pattern.format(wordvectorname, name).lower()
    plt.savefig(path_dir+img_file_name)


def show_percentage(x):
    return "{0:.2f}%".format(round(x, 2) * 100)


def log_wiki_result(name, wordVecName, ac_value, f1_value, pr_value, re_value, foldername, f):

    github_url = "https://github.com/yeetornghoo/SocialMovementSentiment/blob/master/dataset/labeled/"
    img_file_name = confusion_matrix_file_name_pattern.format(wordVecName, name).lower()
    cfm_file_url = "![]({}{}/img/validation/0_preliminary/{})".format(github_url, foldername, img_file_name)

    line_msg = "| {} |  {} |  {} |  {} |  {} | {} |".format("{} with {}".format(name, wordVecName), ac_value, f1_value, pr_value, re_value, cfm_file_url)
    f.write(line_msg+"\n")


def run_ml_repeatedkfold(wordVecName, wordVecObj, df, X, y, clf, clf_name, path_dir, f):

    print(f'Spliting Type   : repeatedkfold')

    v_X = wordVecObj.fit_transform(X)
    # TEST MODEL
    rkf = RepeatedKFold(n_splits=5, n_repeats=2, random_state=12883823)

    fold_number = 1
    ac_scores = []
    f1_scores = []
    pr_scores = []
    re_scores = []

    for train_index, test_index in rkf.split(df):

        X_train, X_test = X[train_index], X[test_index]  # FEATURES
        y_train, y_test = y[train_index], y[test_index]  # CLASSES

        # TRAINING SET
        v_X_train = wordVecObj.transform(X_train)
        clf.fit(v_X_train, y_train)

        # PREDICTION
        v_X_test = wordVecObj.transform(X_test)
        fold_pred = clf.predict(v_X_test)
        ac_scores.append(accuracy_score(y_test, fold_pred))
        f1_scores.append(f1_score(y_test, fold_pred, average='macro'))
        pr_scores.append(precision_score(y_test, fold_pred, average='macro'))
        re_scores.append(recall_score(y_test, fold_pred, average='macro'))

        fold_number += 1

    LogController.log("Result")
    LogController.log('Accuracy score: {}'.format(round(mean(ac_scores), 4)))
    LogController.log('Testing F1 score: {}'.format(round(mean(f1_scores), 4)))
    LogController.log('Testing Precision score: {}'.format(round(mean(pr_scores), 4)))
    LogController.log('Testing Recall score: {} \n'.format(round(mean(re_scores), 4)))

    log_wiki_result(clf_name, wordVecName, round(mean(ac_scores), 4), round(mean(f1_scores), 4),
                    round(mean(pr_scores), 4), round(mean(re_scores), 4), path_dir, f)

    # CONFUSION MATRIC
    confusion_matrix(clf, v_X, y, clf_name, wordVecName, df, path_dir)

    # SAVE MODEL
    filename = path_dir + ("model_{}_{}.sav".format(clf_name, wordVecName)).lower()
    pickle.dump(clf, open(filename, 'wb'))


def run_machine_learnings(wordVecName, wordVecObj, df, X, y, path_dir):

    # DEFINE MACHINE LEARNING MODEL
    clf_dict = {
        'MultinomialNB': MultinomialNB(),
        'SVN': svm.SVC(C=1.0, kernel='rbf', degree=3, gamma='scale', coef0=0.0, shrinking=True, probability=False,
                       tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=2000,
                       decision_function_shape='ovr', random_state=2),
        'LinearSVC': LinearSVC(penalty='l2', loss='squared_hinge', dual=True, tol=0.001, C=1.0, multi_class='ovr',
                               fit_intercept=True, intercept_scaling=1, class_weight=None, verbose=0, random_state=None,
                               max_iter=30000)
    }

    f = open(path_dir + "result.txt", "a")
    f.truncate(0)

    for clf_name, clf in clf_dict.items():
        print(f'ML Name         : {clf_name}')
        print(f'Vector Name     : {wordVecName}')
        run_ml_repeatedkfold(wordVecName, wordVecObj, df, X, y, clf, clf_name, path_dir, f)


def run_bow(df, X, y, path_dir):

    LogController.log_h1("CHECK BOW WORD VECTOR")
    BOW = CountVectorizer()
    BOW.fit_transform(X)

    # RUN MACHINE LEARNING
    run_machine_learnings("BOW", BOW, df, X, y, path_dir)

    # SAVE VECTOR
    pickle.dump(BOW, open(path_dir+"bow.pickle", "wb"))


def run_tfidf(df, X, y, path_dir):
    LogController.log_h1("CHECK TF-IDF WORD VECTOR")
    TFIDF = TfidfVectorizer()
    TFIDF.fit_transform(X)

    # RUN MACHINE LEARNING
    run_machine_learnings("TF-IDF", TFIDF, df, X, y, path_dir)

    # SAVE VECTOR
    pickle.dump(TFIDF, open(path_dir+"tfidf.pickle", "wb"))


def run(df, foldername):

    path_dir = foldername + "/img/validation/0_preliminary/"
    FolderHelper.reset_folder(path_dir)

    X = df['tweet_text'].values.astype('U')
    y = df['sentiment'].values

    run_bow(df, X, y, path_dir)
    run_tfidf(df, X, y, path_dir)

<<<<<<< HEAD
=======
    #f.close()
>>>>>>> 0ef7149a4f4542024eae32835c5a34a92fea8bf7


