from paretoset import paretoset
import pandas as pd

def get_paretoset_scores(data, sense):
    suppliers = pd.DataFrame(data)
    mask = paretoset(suppliers, sense=sense)
    return suppliers[mask].index.to_list()

# hotels = pd.DataFrame({"price": [50, 53, 62, 87, 83, 39, 60, 44],
#                        "distance_to_beach": [13, 21, 19, 13, 5, 22, 22, 25],
#                        })
# mask = paretoset(hotels, sense=["min", "max"])
# paretoset_hotels = hotels[mask]
# print(paretoset_hotels.index.to_list())
