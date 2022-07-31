import pulp
import pandas as pd

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







