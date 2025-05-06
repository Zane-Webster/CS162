names = ["Bob", "Suzie", "Mary", "Trieste", "Bill", "James", "Dylan", "Michael", "Alice", "Deanna"]

hash_table = []
for name in names:
    hash_table.append([hash(name), name])

print(hash_table)

"""
SELECT E.Name, J.JobTitle, J.SkillCode
FROM EMPLOYEE E
JOIN JOB J
ON E.JobId = J.JobId
"""

