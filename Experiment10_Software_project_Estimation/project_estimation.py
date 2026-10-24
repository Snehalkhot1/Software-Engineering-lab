
# Software Project Estimation Techniques

def estimate_by_expert():
    print("\n1. Expert Judgment")
    effort = 20
    cost_per_day = 1500
    cost = effort * cost_per_day
    print("Estimated effort:", effort, "person-days")
    print("Estimated cost: Rs.", cost)


def estimate_by_analogy():
    print("\n2. Estimation by Analogy")
    previous_project_days = 25
    similarity = 0.80
    estimated_days = previous_project_days * similarity
    print("Estimated effort:", estimated_days, "person-days")


def estimate_by_loc():
    print("\n3. Lines of Code (LOC)")
    estimated_lines = 1000
    productivity = 50
    effort = estimated_lines / productivity
    print("Estimated effort:", effort, "person-days")


def estimate_by_function_points():
    print("\n4. Function Point Estimation")
    function_points = 100
    productivity = 5
    effort = function_points / productivity
    print("Estimated effort:", effort, "person-days")


def estimate_by_cocomo():
    print("\n5. COCOMO Model")
    # Basic COCOMO: Effort = 2.4 * (KLOC ** 1.05)
    kloc = 5
    effort = 2.4 * (kloc ** 1.05)
    print("Estimated effort:", round(effort, 2), "person-months")


print("SOFTWARE PROJECT ESTIMATION")
estimate_by_expert()
estimate_by_analogy()
estimate_by_loc()
estimate_by_function_points()
estimate_by_cocomo()
