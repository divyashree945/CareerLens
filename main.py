# CareerLens - Basic Skill Gap Analyzer

your_skills = ["Python", "Java", "C"]

job_skills = ["Python", "SQL", "Machine Learning", "Statistics"]

matched_skills = []
missing_skills = []

for skill in job_skills:
    if skill in your_skills:
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)

match_percentage = (len(matched_skills) / len(job_skills)) * 100

print("CareerLens - Skill Gap Report")
print("Matching skills:", matched_skills)
print("Skills to learn:", missing_skills)
print("Job skill match:", match_percentage, "%")
