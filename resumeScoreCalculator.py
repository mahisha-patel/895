import json

class ResumeScoreCalculator:

  def calculateResumeScores(self, model, job, resumes, n=10):
    resumeScores = dict()
    for i in range(n):
      resume = resumes[i]
      serialized_resume = serialized_resume = {k: v if isinstance(v, (int, float, str, list, dict, tuple)) else str(v) for k, v in resume.items()}
      score = model.generate_content(f"You are a very intelligent recruiter helping to shortlist most qualified candidated \
      based on a job description. You are given a job description and resume, you will generate a score by performing semantic \
      matching on entire content of resume and JD. \
      JD: {json.dumps(job)}, Resume: {json.dumps(serialized_resume)} Now generate a numerical score out of 10 by \
      matching the skills, title, experience, academics, citizenship and qualifications required for the job based on \
      candidate's resume (10 if most of the things are matched). Just return a score, nothing else.")
      resumeScores[i] = score.text

    return resumeScores