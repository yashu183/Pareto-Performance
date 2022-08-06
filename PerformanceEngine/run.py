from utils.engine import get_overall_score

filters = {
    "Service": "Applications Development",
}
attributes = {
    "Rating": {
        "Objective": "Maximize",
        "Weightage": 30,
        "tends_to_value": 100,
    },
    "Resources": {
        "Objective": "Minimize",
        "Weightage": 10,
        "tends_to_value": 1,
    },
    "Avg. Cost($)": {
        "Objective": "Minimize",
        "Weightage": 25,
        "tends_to_value": 1,
    },
    "Average Delivery Time": {
        "Objective": "Minimize",
        "Weightage": 20,
        "tends_to_value": 1,
    },
    "Number of Escalations": {
        "Objective": "Minimize",
        "Weightage": 15,
        "tends_to_value": 1,
    }
}
json_data_path = f'/Users/vigneswaran/Projects/sirion/SupplierPerformance/sample_data/{filters["Service"]}.json'
print(get_overall_score(json_data_path, filters, attributes))
