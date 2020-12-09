import pandas as pd
import numpy as np
from floodFill import floodFill

randomDf = np.random.randint(0,3,size=(15   ,15))

print(randomDf)

import time
start_time = time.time()
regions = floodFill(randomDf)

print("--- %s seconds ---" % (time.time() - start_time))