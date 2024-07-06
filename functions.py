
import pandas as pd

#########################
def compute_features(df):

    df = df.copy()
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['quarter'] = df.index.quarter
    df['semester'] = np.where(df['quarter'] > 2,2,1)
    df['month'] = df.index.month

    return df
    #########

##################################################################
def split_train_test(la_mia_serie, date_of_division = '2020-04-01'):

  train = la_mia_serie.loc[la_mia_serie.index < date_of_division]
  test = la_mia_serie.loc[la_mia_serie.index >= date_of_division]

  return train, test
  ##################


#########################################
def build_test_set(one_serie):

  last_date = one_serie.index.max()

  next_four = [last_date + pd.DateOffset(months=i) for i in range(1, 5)]
  new_data = pd.DataFrame(next_four, columns=['date'])
  new_data = new_data.set_index('date')
  
  return compute_features(new_data)
  ##################################


#########################################
def save_results(datadict, filename):

  results_df = pd.DataFrame(datadict)

  results_df['id'] = results_df['year'].astype(str)+ '_' +results_df['month'].astype(str)+ '_' + results_df['custom_id']

  volumes = results_df['volume_kg']  
  cols_to_drop = ['custom_id', 'year', 'month', 'volume_kg']

  results_df = results_df.drop(columns=cols_to_drop)
  results_df['volume_kg']  = volumes 

  results_df.to_csv(f'{filename}.csv', index=False)

  print(f'>> Saved {filename+".csv":>21} - shape: {results_df.shape} - {list(results_df.columns)}')

  return results_df
  ##################

