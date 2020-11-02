from Controller import FileController, LogController
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn import svm
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import RepeatedKFold
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

path_dir = "img/validation/0_preliminary/"
f = open(path_dir+"result.txt", "a")
f.truncate(0)
confusion_matrix_file_name_pattern = "{}_{}_confusion_matrix.png"
parent_folder = ""


def confusion_matrix(classifier, X, y, name, wordvectorname, df):
    class_names = df.sentiment.unique()

    disp = plot_confusion_matrix(classifier, X, y, display_labels=class_names, cmap=plt.cm.Blues)

    plt.title("Confusion matrix of {} {}".format(wordvectorname, name))

    img_file_name = confusion_matrix_file_name_pattern.format(wordvectorname, name).lower()
    plt.savefig(path_dir+img_file_name)


def show_percentage(x):
    return "{0:.2f}%".format(round(x, 2) * 100)


def log_wiki_result(name, wordVecName, ac_value, f1_value, pr_value, re_value, foldername):

    github_url = "https://github.com/yeetornghoo/SocialMovementSentiment/blob/master/dataset/labeled/"
    img_file_name = confusion_matrix_file_name_pattern.format(wordVecName, name).lower()
    cfm_file_url = "{}{}/img/validation/0_preliminary/{}".format(github_url, foldername, img_file_name)

    line_msg = "| {} |  {} |  {} |  {} |  {} | {} |".format("{} with {}".format(name, wordVecName), ac_value, f1_value, pr_value, re_value, cfm_file_url)
    f.write(line_msg+"\n")


def run_ML(wordVecName, wordVecObj, df, X, y, foldername):

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

    for name, clf in clf_dict.items():

        # TRAIN MODEL
        random_state = 12883823
        rkf = RepeatedKFold(n_splits=2, n_repeats=2, random_state=random_state)

        icount = 0
        for train_index, test_index in rkf.split(df):
            X_train, X_test = X[train_index], X[test_index]  # FEATURES
            y_train, y_test = y[train_index], y[test_index]  # CLASSES

            # TRAINING SET
            v_X_train = wordVecObj.transform(X_train)  # FEATURE TRAINING SET
            clf.fit(v_X_train, y_train)

            icount += 1

        v_X_test = wordVecObj.transform(X)
        pred = clf.predict(v_X_test)

        ac_value = round(accuracy_score(y, pred), 4)
        f1_value = round(f1_score(y, pred, average='macro'), 4)
        pr_value = round(precision_score(y, pred, average='macro'), 4)
        re_value = round(recall_score(y, pred, average='macro'), 4)

        LogController.log("Result of {} with {}".format(name, wordVecName))
        LogController.log('Testing accuracy: {}'.format(show_percentage(accuracy_score(y, pred))))
        LogController.log('Testing F1 score: {}'.format(show_percentage(f1_score(y, pred, average='macro'))))
        LogController.log('Testing Precision score: {}'.format(show_percentage(precision_score(y, pred, average='macro'))))
        LogController.log('Testing Recall score: {} \n'.format(show_percentage(recall_score(y, pred, average='macro'))))

        log_wiki_result(name, wordVecName, ac_value, f1_value, pr_value, re_value, foldername)

        confusion_matrix(clf, v_X_test, y, name, wordVecName, df)


def run_bow(df, X, y, foldername):
    LogController.log_h1("CHECK BOW WORD VECTOR")
    BOW = CountVectorizer()
    BOW.fit_transform(X)
    run_ML("BOW", BOW, df, X, y, foldername)


def run_tfidf(df, X, y, foldername):
    LogController.log_h1("CHECK TF-IDF WORD VECTOR")
    TFIDF = TfidfVectorizer()
    TFIDF.fit_transform(X)
    run_ML("TF-IDF", TFIDF, df, X, y, foldername)


def run(df, foldername):
    X = df['tweet_text'].values
    y = df['sentiment'].values

    run_bow(df, X, y, foldername)
    run_tfidf(df, X, y, foldername)

    f.close()


