
import datetime as dt
import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error


def str_to_date(text: str) -> dt.datetime:
    splitted = text.split("_")
    return dt.datetime(int(splitted[0]), int(splitted[1]), 1)



def solution_to_global(df: pd.DataFrame, row_id_column_name: str) -> pd.Series:

    return (df.assign( date=df[row_id_column_name].map(str_to_date))
            [["date", "volume_kg"]].groupby("date")["volume_kg"].sum().sort_index())



def mape_score(solution: pd.DataFrame, submission: pd.DataFrame, row_id_column_name: str) -> float:
    mape = mean_absolute_percentage_error(solution["volume_kg"].to_numpy(),
                                          submission["volume_kg"].to_numpy(),)

    global_solution = solution_to_global(solution, row_id_column_name)
    global_submission = solution_to_global(submission, row_id_column_name)

    if (global_solution.index != global_submission.index).any(): raise ValueError("index")

    global_mape = mean_absolute_percentage_error(global_solution.to_numpy(),global_submission.to_numpy())

    return (3 * mape + global_mape) / 4



