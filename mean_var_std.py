import numpy as np

def calculate(list):
  
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
    
  listn = np.array(list)

  mean_col = [listn[[0,3,6]].mean(), listn[[1,4,7]].mean(), listn[[2,5,8]].mean()]  
  mean_row = [listn[[0,1,2]].mean(), listn[[3,4,5]].mean(), listn[[6,7,8]].mean()]
  mean_flat = listn.mean()
  
  var_col = [listn[[0,3,6]].var(), listn[[1,4,7]].var(), listn[[2,5,8]].var()]
  var_row = [listn[[0,1,2]].var(), listn[[3,4,5]].var(), listn[[6,7,8]].var()]
  var_flat = listn.var()

  std_col = [listn[[0,3,6]].std(), listn[[1,4,7]].std(), listn[[2,5,8]].std()]
  std_row = [listn[[0,1,2]].std(), listn[[3,4,5]].std(), listn[[6,7,8]].std()]
  std_flat = listn.std()

  max_col = [listn[[0,3,6]].max(), listn[[1,4,7]].max(), listn[[2,5,8]].max()]
  max_row = [listn[[0,1,2]].max(), listn[[3,4,5]].max(), listn[[6,7,8]].max()]
  max_flat = listn.max()

  min_col = [listn[[0,3,6]].min(), listn[[1,4,7]].min(), listn[[2,5,8]].min()]
  min_row = [listn[[0,1,2]].min(), listn[[3,4,5]].min(), listn[[6,7,8]].min()]
  min_flat = listn.min()

  sum_col = [listn[[0,3,6]].sum(), listn[[1,4,7]].sum(), listn[[2,5,8]].sum()]
  sum_row = [listn[[0,1,2]].sum(), listn[[3,4,5]].sum(), listn[[6,7,8]].sum()]
  sum_flat = listn.sum()

  return {
      'mean': [mean_col, mean_row, mean_flat],
      'variance': [var_col, var_row, var_flat],
      'standard deviation': [std_col, std_row, std_flat],
      'max': [max_col, max_row, max_flat],
      'min': [min_col, min_row, min_flat],
      'sum': [sum_col, sum_row, sum_flat]
  }
