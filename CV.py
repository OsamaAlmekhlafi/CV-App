class Experience:
    def __init__(self, company, job_title, start_date, end_date):
        self.company = company
        self.job_title = job_title
        self.start_date = start_date
        self.end_date = end_date

    def display_experience(self):
        print(f"Company: {self.company}")
        print(f"Job Title: {self.job_title}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print()


class Education:
    def __init__(self, degree, institution, completion_date):
        self.degree = degree
        self.institution = institution
        self.completion_date = completion_date

    def display_education(self):
        print(f"Degree: {self.degree}")
        print(f"Institution: {self.institution}")
        print(f"Completion Date: {self.completion_date}")
        print()


class Skill:
    def __init__(self, skill, percentage):
        self.skill = skill
        self.percentage = percentage

    def display_skill(self):
        print(f"Skill: {self.skill}")
        print(f"Percentage: {self.percentage}%")
        print()


class CV:
    def __init__(self):
        self.experiences = []
        self.education = []
        self.skills = []

    def add_experience(self):
        company = input("Enter the company name: ")
        job_title = input("Enter the job title: ")
        start_date = input("Enter the start date: ")
        end_date = input("Enter the end date: ")

        experience = Experience(company, job_title, start_date, end_date)
        self.experiences.append(experience)

        add_more = input("Do you want to add another experience? (yes/no): ")
        if add_more.lower() == "yes" or add_more.lower() == "y":
            self.add_experience()

    def add_education(self):
        degree = input("Enter the degree: ")
        institution = input("Enter the institution: ")
        completion_date = input("Enter the completion date: ")

        education = Education(degree, institution, completion_date)
        self.education.append(education)

        add_more = input("Do you want to add another education? (yes/no): ")
        if add_more.lower() == "yes" or add_more.lower() == "y":
            self.add_education()

    def add_skill(self):
        skill = input("Enter the skill: ")
        percentage = input("Enter the skill percentage: ")

        skill = Skill(skill, percentage)
        self.skills.append(skill)

        add_more = input("Do you want to add another skill? (yes/no): ")
        if add_more.lower() == "yes" or add_more.lower() == "y":
            self.add_skill()

    def display_cv(self):
        print("Here is CV")
        print("-------------")
        print("Experiences:")
        for experience in self.experiences:
            experience.display_experience()

        print("Education:")
        for education in self.education:
            education.display_education()

        print("Skills:")
        for skill in self.skills:
            skill.display_skill()


name = input("Enter your name: ")
cv = CV()

add_skills = input("Do you want to add skills? (yes/no): ")
if add_skills.lower() == "yes" or add_skills.lower() == "y":
    cv.add_skill()

add_educations = input("Do you want to add educations? (yes/no): ")
if add_educations.lower() == "yes" or add_educations.lower() == "y":
    cv.add_education()

add_experiences = input("Do you want to add experiences? (yes/no): ")
if add_experiences.lower() == "yes" or add_experiences.lower() == "y":
    cv.add_experience()

print(f"\n\t Welcome {name} Your CV is : \n")
cv.display_cv()
