import json

class JobScoreCalculator:
    
    def calculateJobScores(self, model, jobs, resume, n=10):
        job_scores = dict()

        for i in range(n):
            job = jobs.iloc[i].to_dict()  # Convert job description to dictionary
            
            # Check if citizenship requirement matches
            if resume['citizenship'] == "No" and job['citizenship_required'] == "Yes":
                job_scores[i] = 0
                continue
            
            # Check if experience requirement matches
            job_experience = job['required_experience_in_months'] // 12
            if job_experience < int(resume['experience_years']) - 1 or job_experience > int(resume['experience_years']) + 1:
                job_scores[i] = 0
                continue
            
            # Generate score by performing semantic matching
            score = model.generate_content(f"You are given a job description and resume, you will generate a score by performing semantic \
                matching on entire content of resume and JD. JD: {json.dumps(job)} Resume: {json.dumps(resume)} \
                Generate a numerical score out of 10 by matching the skills, title, experience, academics and qualifications required \
                for the job based on candidate's resume (10 if most of the skills are matched). Just return a numerical score in output, nothing else. \
                Assess and match the title of the job, that will provide the information about the Job Seniority Level and also the domain \
                For ex: Staff Software Engineer in Test describes that it is a high level position and can't have candidates having under than \
                minimum of 5 years of experience, requires someone from Test background. The other thing is the skills of the candidate \
                should matter heavily in scoring, if the candidate don't have around half of the skills mentioned in the JD, then that \
                candidate should have low score. For ex: JD skills: Python, Django, Flask, SQL. Resume have Python, Flask and SQL should have\
                higher score. Think step by step but Remember to return only a numerical score in answer.")
                
            # Store the score
            job_scores[i] = score.text

        return job_scores