from jobFinder import JobFinder
from resumeFinder import ResumeFinder
import google.generativeai as genai # type: ignore
import pandas as pd # type: ignore
import json


class RoleFinder:
    def __init__(self):
        pass

    def getRole(self):
        role = input('Who are you? Type 1 or 2 \n1. Recruiter \n2. Candidate\n')
        
        genai.configure(api_key='XXX')
        safety_settings = [
            {
                "category": "HARM_CATEGORY_DANGEROUS",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ]
        model = genai.GenerativeModel('gemini-pro', safety_settings=safety_settings)

        with open('/Users/patron/Downloads/895/alumni_resume6', 'r') as f:
            resumes = json.load(f)

        jobs = pd.read_csv('/Users/patron/Downloads/895/895-Jobs-final.csv')

        if role == '1':
            job = jobs.iloc[80].to_dict()
            resumeFind = ResumeFinder()
            resumeFind.getFinalResult(model, job, resumes, 25)
        elif role == '2':
            with open('/Users/patron/Downloads/895/alumni_company_linkedin5.json', 'r') as file:
                alumniCompanyLinkedinData = json.load(file)
            getResult = JobFinder()
            getResult.getFinalResult(model, jobs, resumes[64], alumniCompanyLinkedinData)
        else:
            print('Please enter a valid number.\n')
            self.getRole()


RoleFinder().getRole()

