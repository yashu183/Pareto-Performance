import pulp


def get_scores(suppliers, data, objective, tends_to_value):
    supplier = pulp.LpVariable.dicts("supplier", suppliers, lowBound=0, cat='Integer')
    objective_fn = pulp.lpSum([(supplier[i] * (data[i]))] for i in suppliers)

    # Create the 'prob' variable to contain the problem data
    prob = pulp.LpProblem("Supplier_Performance_Problem", pulp.LpMaximize if objective == "Maximize" else pulp.LpMinimize)

    # The objective function is added to 'prob' first
    prob += objective_fn

    # The constraints are added to 'prob'
    if objective == "Maximize":
        prob += objective_fn <= tends_to_value
    else:
        prob += objective_fn >= tends_to_value

    pulp.PULP_CBC_CMD(msg=False).solve(prob)

    scores = {}

    for v in prob.variables():
        name = v.name[9:]
        try:
            scores[name] = v.varValue
        except Exception as e:
            print(f'v.varValue None {e}')
            scores[name] = 0

    return scores


def get_optimal_supplier(data: dict, attributes: dict, order: list):
    """
    Returns list of the best supplier based on the prioritized attributes
    :param data: Dataframe that contains all the values of the attributes like (Supplier Name, Region, Country)
    :type data: Dataframe
    :param attributes: List of dictionary which provides the attribute as key
    along with maximum/minimum expected value and objective (Maximize/Minimize)
    :type attributes: Dictionary
    :param order: Order for Optimisation
    :type: List
    :return: list of the best supplier based on the prioritized attributes
    :rtype: List
    """
    # {
    #     "Supplier Name": "Infosys",
    #     "Region": "APAC",
    #     "Country": "India",
    #     "Function": "IT & Infrastructure",
    #     "Service": "Applications Development",
    #     "Avg. Cost($)": "100k",
    #     "Rating": "90",
    #     "Average Delivery Time": "90",
    #     "Number of Escalations": "5",
    #     "Year": "2018",
    #     "Resources": "10000"
    # },
    pass
