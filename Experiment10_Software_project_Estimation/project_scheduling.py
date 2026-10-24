
# Software Project Scheduling Techniques

tasks = [
    ("Requirement Analysis", 3),
    ("System Design", 4),
    ("Coding", 8),
    ("Testing", 4),
    ("Deployment", 2)
]

print("SOFTWARE PROJECT SCHEDULE")
print("-" * 45)

total_days = 0

for task, duration in tasks:
    start_day = total_days + 1
    end_day = total_days + duration

    print(task)
    print("Duration:", duration, "days")
    print("Start Day:", start_day)
    print("End Day:", end_day)
    print("-" * 45)

    total_days += duration

print("Total project duration:", total_days, "days")
