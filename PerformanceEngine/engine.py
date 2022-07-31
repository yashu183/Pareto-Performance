from PerformanceEngine.lp_helper import get_optimal_supplier

sample_data = [
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

attributes = {
    "Rating": {
        "Objective": "Maximize",
        "tends_to_value": 100,
        "priority": 1
    },
    "Country": {
        "Objective": None,
        "tends_to_value": "India",
        "priority": 0
    },
    "Service": {
        "Objective": None,
        "tends_to_value": "Applications Development",
        "priority": 0
    },
    "Avg. Cost($)": {
        "Objective": "Minimize",
        "tends_to_value": 100_000,
        "priority": 2
    },
    "Average Delivery Time": {
        "Objective": "Minimize",
        "tends_to_value": 30,
        "priority": 3
    },
    "Number of Escalations": {
        "Objective": "Minimize",
        "tends_to_value": 0,
        "priority": 4
    }
}

order = ["Rating", "Avg. Cost($)", "Average Delivery Time", "Number of Escalations"]

print(get_optimal_supplier(sample_data, attributes))
