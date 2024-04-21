class RecommendationGenerator:
    def generateCoverLetterPoint(self, model, job, resume):
        return model.generate_content(f"Give some unique point from the candidate's resume to highlight \
            in the cover letter while applying to this job: {job}, Resume: {resume}")

    def generateLinkedinMsg(self, model, job, alumni_company_linkedin_data):
        return model.generate_content(f"Please generate a customized LinkedIn connection request note strictly under 300 \
            characters to send to the alumni of your past/present university {alumni_company_linkedin_data[job['employer_name']][0]} \
            who works/worked at {job['employer_name']} to seek guidance for the job {job['job_title']} at {job['employer_name']}. \
            Do not mention if the message is from a past of current student of that university.")
