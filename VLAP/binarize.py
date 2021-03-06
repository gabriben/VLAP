# I should do this on all Ys

from sklearn.preprocessing import MultiLabelBinarizer

def binarize(y_train, y_val, y_test):
    
    # Fit the multi-label binarizer on the training set
    print("Labels:")
    mlb = MultiLabelBinarizer()
    mlb.fit(y_train)

    # Loop over all labels and show them
    N_LABELS = len(mlb.classes_)
    for (i, label) in enumerate(mlb.classes_):
        print("{}. {}".format(i, label))

    # transform the targets of the training and test sets
    y_train_bin = mlb.transform(y_train)
    y_val_bin = mlb.transform(y_val)
    y_test_bin = mlb.transform(y_test)

    return(y_train_bin, y_val_bin, y_test_bin, N_LABELS)

