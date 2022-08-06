from lp_helper import get_scores

supplier_data = [
    {
        "Supplier Name": "Infosys",
        "Region": "APAC",
        "Country": "India",
        "Function": "IT & Infrastructure",
        "Service": "Applications Development",
        "Avg. Cost($)": 100_000,
        "Rating": 90,
        "Average Delivery Time": "90",
        "Number of Escalations": "5",
        "Year": "2018",
        "Resources": "10000"
    },
    {
        "Supplier Name": "Genpact",
        "Region": "North America",
        "Country": "United States",
        "Function": "Consulting",
        "Service": "Applications Development & Maintenance",
        "Avg. Cost($)": 150_000,
        "Rating": 80,
        "Average Delivery Time": "180",
        "Number of Escalations": "40",
        "Year": "2017",
        "Resources": "6000"
    },
    {
        "Supplier Name": "IBM",
        "Region": "North America",
        "Country": "United States",
        "Function": "IT & Infrastructure",
        "Service": "Mainframe services",
        "Avg. Cost($)": 150_000,
        "Rating": 85,
        "Average Delivery Time": "180",
        "Number of Escalations": "100",
        "Year": "2014",
        "Resources": "8000",
    },
    {
        "Supplier Name": "Capgemini",
        "Region": "Europe",
        "Country": "France",
        "Function": "HR",
        "Service": "Service Desk",
        "Avg. Cost($)": 100_000,
        "Rating": 85,
        "Average Delivery Time": "270",
        "Number of Escalations": "150",
        "Year": "2016",
        "Resources": "5000",
    }
]

overall_scores = {}
for idx, supplier in enumerate(supplier_data):
    supplier['score'] = 0
    supplier['id'] = "supplier_{}".format(idx)
    overall_scores[supplier['id']] = 0

attributes = {
    "Rating": {
        "Objective": "Maximize",
        "tends_to_value": 100,
    },
    "Avg. Cost($)": {
        "Objective": "Minimize",
        "tends_to_value": 1,
    },
    "Average Delivery Time": {
        "Objective": "Minimize",
        "tends_to_value": 1,
    },
    "Number of Escalations": {
        "Objective": "Minimize",
        "tends_to_value": 1,
    }
}

# Get Scores using paretoset logic



# Get Scores using Linear Programming
attribute_wise_score = {}

for key, value in attributes.items():
    suppliers = []
    all_constants = {}

    for i in supplier_data:
        suppliers.append(i["id"])
        all_constants[i["id"]] = int(i[key])

    result = get_scores(suppliers,
                        all_constants,
                        value["Objective"],
                        value["tends_to_value"])
    print(result)
    for v, s in result.items():
        overall_scores[v] += s
        attribute_wise_score[key] = result

print(overall_scores)
print(attribute_wise_score)

# print(get_optimal_supplier(sample_data, attributes))
