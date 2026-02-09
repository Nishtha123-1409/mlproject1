import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder , StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):

        #this function will convert all categorical feat to numerical feat
        try:
            numerical_columns = [ 'reading_score', 'writing_score']
            categorical_columns= ['gender', 'race_ethnicity', 'parental_level_of_education', 
                                    'lunch', 'test_preparation_course']
            
            #creating numeric pipeline for missing values,std scalrer
            num_pipelinie=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )
            #creating categorical pipeline
            cat_pipeline=Pipeline(
                steps=[
                    ("impute",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]
            )
            logging.info(f"categorical columns: {categorical_columns}")
            logging.info(f"numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipelinie,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor


        except Exception as e: #custom exception
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info('Reading train and test data is completed.')
            logging.info('obataining preprocessing info.')

            preprocessor_obj=self.get_data_transformer_object()

            target_column_name = "math score"
            numerical_columns = [ 'reading_score', 'writing_score']

            input_feature_train_df= train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df= train_df[target_column_name]


            input_feature_test_df= test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df= test_df[target_column_name]


            logging.info(
                f"Applying preprocessing object on training and testing data frame."
            )

            input_feature_train_array = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_array = preprocessor_obj.fit_transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_array , np.array(target_feature_train_df)
            ] 
            #np.c_:It concatenates input features and target values 
            # column-wise to form a single training array where the last
            #  column represents the target.” 
            test_arr = np.c_[
                input_feature_test_array , np.array(target_feature_test_df)
            ] 

            logging.info(f"saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
          


            
        except Exception as e:
            raise CustomException(e, sys)
            