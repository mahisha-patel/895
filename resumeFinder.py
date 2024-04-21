from resumeScoreCalculator import ResumeScoreCalculator
import pprint

class ResumeFinder:

  def getFinalResult(self, model, job, resumes, n=10):
    resumeScoreCalc = ResumeScoreCalculator()
    resumeScores = resumeScoreCalc.calculateResumeScores(model, job, resumes, n)
    sortedResumeScores = dict(sorted(resumeScores.items(), key=lambda item: float(item[1]), reverse=True))

    print("Sorted Resume scores (descending):")
    print(sortedResumeScores, "\n")

    with open("results_resumes.txt", "w") as file:
            # Write content to the file
            file.write(f"{sortedResumeScores}\n")

    for k, v in sortedResumeScores.items():
      if float(v) != 0.0 or float(v) != 0:  # Check for non-zero scores
        pprint.pprint(resumes[k])