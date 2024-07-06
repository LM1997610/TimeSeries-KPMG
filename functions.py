
import pandas as pd

def build_test_set(one_serie, compute_features):

  last_date = one_serie.index.max()

  next_four = [last_date + pd.DateOffset(months=i) for i in range(1, 5)]
  new_data = pd.DataFrame(next_four, columns=['date'])
  new_data = new_data.set_index('date')
  
  return compute_features(new_data)
 


def save_results(datadict, filename, output_dir='submissions/'):

  results_df = pd.DataFrame(datadict)

  results_df['id'] = results_df['year'].astype(str)+ '_' +results_df['month'].astype(str)+ '_' + results_df['custom_id']

  volumes = results_df['volume_kg']  
  cols_to_drop = ['custom_id', 'year', 'month', 'volume_kg']

  results_df = results_df.drop(columns=cols_to_drop)
  results_df['volume_kg']  = volumes 

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
  results_df.to_csv(f'output_dir+{filename}.csv', index=False)

  print(f'>> Saved {filename+".csv":>21} - shape: {results_df.shape} - {list(results_df.columns)}')

  return results_df


def prediction_plot(this_serie, this_pred, this_serie_name, output_dir = 'plots'):

  plt.figure(figsize=(8, 3.5))

  plt.plot(this_serie['volume_kg'])
  plt.plot(this_pred['volume_kg'], color='r', marker=".", markersize=7, alpha=0.7)

  plt.title('\n'+serie_names[indx]+'\n')

  plt.legend(['Truth', 'Predictions'], loc='upper right')
  plt.ylabel('\n volume_kg \n', fontsize=11)

  plt.grid('-', alpha=0.5)
  plt.xticks(rotation=45)
  plt.tight_layout()

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  plt.savefig(output_dir + f'/{this_serie_name}.png')
  plt.close()
