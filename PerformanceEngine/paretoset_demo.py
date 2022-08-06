from paretoset import paretoset
import pandas as pd

hotels = pd.DataFrame({"price": [50, 53, 62, 87, 83, 39, 60, 44],
                       "distance_to_beach": [13, 21, 19, 13, 5, 22, 22, 25],
                       })
mask = paretoset(hotels, sense=["min", "max"])
paretoset_hotels = hotels[mask]
print(paretoset_hotels)