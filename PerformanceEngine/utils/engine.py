import json
from itertools import chain, combinations
import time

from .lp_helper import get_linear_programming_scores
from .optimisation import get_paretoset_scores
from .constants import paretoset_sense, paretoset_score


def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(2, len(ss)+1)))

def get_overall_score(json_data_path, filters, attributes):
    with open(json_data_path, 'r') as f:
        supplier_data = json.load(f)

    for f in filters:
        if f != "Service":
            supplier_data = [i for i in supplier_data if i[f] == filters[f]]

    overall_scores = {}
    for idx, supplier in enumerate(supplier_data):
        supplier['score'] = 0
        supplier['id'] = "supplier_{}".format(idx)
        overall_scores[idx] = 0

    print(f"Total Competing Suppliers: {len(supplier_data)}")

    paretoset_start = time.time()
    # Get Scores using paretoset logic
    print(f"Running paretoset logic")
    all_combinations = all_subsets(attributes)
    for comb in all_combinations:
        print(f"Running {comb} for paretoset")
        data = {}
        sense = []
        for attribute in comb:
            data[attribute] = []
            for supplier in supplier_data:
                data[attribute].append(supplier[attribute])
            sense.append(paretoset_sense[attributes[attribute]["Objective"]])

        scores = get_paretoset_scores(data, sense)
        for i in scores:
            overall_scores[i] += paretoset_score

    paretoset_end = time.time()
    print(f"Paretoset Completed in {int(paretoset_end - paretoset_start)} seconds")

    lp_start = time.time()
    # Get Scores using Linear Programming
    print(f"Running LP logic")
    for key, value in attributes.items():
        print(f"Running {key} attribute for LP logic")
        suppliers = []
        all_constants = {}
        for i in supplier_data:
            suppliers.append(i["id"])
            all_constants[i["id"]] = int(i[key])

        result = get_linear_programming_scores(suppliers, all_constants, value["Objective"], value["tends_to_value"])
        for v, s in result.items():
            overall_scores[int(v.split("_")[1])] += s

    lp_end = time.time()
    print(f"LP Completed in {int(lp_end - lp_start)} seconds")

    sorted_suppliers = sorted(list(overall_scores.items()), key=lambda i: i[1], reverse=True)
    all_non_zero_scorers = []
    for sup in sorted_suppliers:
        idx, score = sup
        if score == 0:
            break
        all_non_zero_scorers.append({supplier_data[idx]["Supplier Name"]: score})

    return all_non_zero_scorers

# get_overall_score(filters, attributes)

#
# attribute_wise_score = {}
#

# # print(get_optimal_supplier(sample_data, attributes))
