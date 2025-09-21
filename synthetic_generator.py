import numpy as np
import json

np.random.seed(42)

skills = ["Java", "React", "Angular", "Spring Boot"]
priorities = ["Low", "Medium", "High", "Critical"]
dependencies = ["Low", "Medium", "High", "Critical"]
task_types = ["Story", "Bug", "Feature"]
collab_levels = ["Low", "Medium", "High"]

def generate_engineers(n=20):
    engineers = []
    for i in range(n):
        engineer = {
            "engineer_id": i,
            "skills": np.random.choice(skills),
            "collab_ability": np.random.choice(collab_levels),
            "availability_index": int(np.random.randint(10, 30)),
            "impact": int(np.random.randint(5, 15)),
            "module_exposure": int(np.random.randint(1, 10)),
            "efficiency": round(float(np.random.normal(1.0, 0.2)), 2)
        }
        engineers.append(engineer)
    return engineers

def generate_tasks(n=50, sprint_len_days=14):
    tasks = []
    for i in range(n):
        task = {
            "task_id": i,
            "skill_required": np.random.choice(skills),
            "due_date": str(int(np.random.randint(1, sprint_len_days * 86400))),
            "priority": np.random.choice(priorities),
            "dependency_level": np.random.choice(dependencies),
            "module_knowledge": int(np.random.randint(1, 30)),
            "task_type": np.random.choice(task_types)
        }
        tasks.append(task)
    return tasks

engineers = generate_engineers(20)
tasks = generate_tasks(50)

# Save as JSON files
with open("engineer_mock_data.json", "w") as f:
    json.dump(engineers, f, indent=4)

with open("tasks_mock_data.json", "w") as f:
    json.dump(tasks, f, indent=4)

print(engineers[:2])
print(tasks[:2])
