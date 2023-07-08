import numpy as np
from catboost import CatBoostClassifier

# загружаем CatBoost
        clf = CatBoostClassifier()
        clf.load_model('CatBoostClassifier')
        np.savetxt(path_to_the_output_file, clf.predict(input_), fmt = '%d')
