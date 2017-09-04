#   https://stackoverflow.com/questions/8489684/python-subclassing-multiprocessing-process
from multiprocessing import Pool

def pool_job(input_val=0):
  # FYI, multiprocessing.Pool can't guarantee that it keeps inputs ordered correctly
  # dict format is {input: output}...
  return {'pool_job(input_val={0})'.format(input_val): int(input_val)*12}

pool = Pool(5)  # Use 5 multiprocessing processes to handle jobs...
results = pool.map(pool_job, range(0, 12)) # map range(0, 12) into pool_job()
print(results)
