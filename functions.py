
import pandas as pd

def build_test_set(one_serie):

  last_date = one_serie.index.max()

  next_four = [last_date + pd.DateOffset(months=i) for i in range(1, 5)]
  new_data = pd.DataFrame(next_four, columns=['date'])
  new_data = new_data.set_index('date')
  
  return compute_features(new_data)
 


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
