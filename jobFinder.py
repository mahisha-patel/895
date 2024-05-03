from recommendationGenerator import RecommendationGenerator
from jobScoreCalculator import JobScoreCalculator
import pprint

class JobFinder:

    def getFinalResult(self, model, jobs, resume, alumniCompanyLinkedinData):
        resume['citizenship'] = input("Do you have a US citizenship? ")
        resume['experience_years'] = input("How many years of experience do you have? ")
        resume['status'] = input("What is your visa status? ")
        resume['location_preference'] = input("Do you have any location preference? If yes, specify. ")

        jobScoreCalc = JobScoreCalculator()
        job_scores = jobScoreCalc.calculateJobScores(model, jobs, resume, 83)
        sorted_job_scores = dict(sorted(job_scores.items(), key=lambda item: float(item[1]), reverse=True))

        print("Sorted job scores (descending):")
        print(sorted_job_scores, "\n")

        with open("results_jobs.txt", "w") as file:
            # Write content to the file
            file.write(f"{sorted_job_scores}\n")

        recommendation = RecommendationGenerator()

        for k, v in sorted_job_scores.items():
            if float(v) != 0.0 or float(v) != 0: 
                j = jobs.iloc[k].to_dict()
                pprint.pprint(j)
                cover_letter_point = recommendation.generateCoverLetterPoint(model, j, resume)
                print("Cover Letter highlight: ", cover_letter_point.text, "\n")
                if j['employer_name'] in alumniCompanyLinkedinData.keys():
                    print("Contact for Reference/Guidance: ", alumniCompanyLinkedinData[j['employer_name']])
                    linkedin_msg = recommendation.generateLinkedinMsg(model, j, alumniCompanyLinkedinData)
                    print(linkedin_msg.text)
                print('*******************************************************************')
