from features import bert
from read_config import read_config

import numpy as np
import pandas as pd
import time
    
def main():
    start_time = time.time()
    type_, path_of_incoming_file, path_to_the_output_file = read_config() # считывает данные из файла config.txt
    input_ = pd.read_csv(path_of_incoming_file)                           # загружаем признаки отзывов из файла
    
    
    if type_ == 'simple':                                                 # если выбрано простое решение
        input_ = input_.drop('text', axis = 1)
        from joblib import load
        clf = load('../models/LogisticRegression.joblib')
        np.savetxt(path_to_the_output_file , clf.predict(input_), fmt = '%d')
        print(time.time()-start_time)
        
    else: # type == 'hard'                                                # если выбрано сложное решение
        input_ = bert(input_)                                             # добавляет в dataset emb57 
        
        from catboost import CatBoostClassifier                           # загружаем CatBoost
        clf = CatBoostClassifier()
        clf.load_model('../models/CatBoostClassifier')
        np.savetxt(path_to_the_output_file, clf.predict(input_), fmt = '%d')
        print(time.time()-start_time)
        
        
if __name__ == "__main__":
    main()
