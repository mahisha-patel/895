## Project for 895: Optimizing the Search Landscape: A Candidate-Centric and Recruiter-Friendly Approach Using Large Language Model

### Overview
This project leverages Large Language Models (LLM) and an alumni network database to enhance job matching, cover letter customization, and networking, delivering a tailored job search experience for job seekers and recruiters.

### Key Features
#### N-Best Matching
Our N-Best Matching system uses LLM to analyze job descriptions and resumes in-depth, going beyond keywords to include factors like skills, experience, and visa status. This method identifies the top 'N' relevant job postings and candidates, ensuring precise and meaningful matches.

#### Data-Driven Cover Letter Customization
Our platform assists job seekers in crafting compelling cover letters by highlighting qualifications that align closely with job requirements, increasing visibility and impact in the hiring process.

#### Targeted Networking through Alumni Network
Integrate professional networking into your job search by connecting with alumni in target companies. Access relevant profiles and personalized communication strategies to seek guidance and gain insights.

### Getting Started
Follow the setup instructions below to implement the platform and begin optimizing your recruitment or job search efforts.

#### Clone this repo on your local machine:
```https://github.com/mahisha-patel/895.git```

#### Install required python packages:
```pip install -r requirements.txt```

#### Setup your Gemini Pro API key
You will require to first obtain an API key for using Gemini-Pro. If you don't already have one, create a key with one click in Google AI Studio. Generate API Key from here: https://aistudio.google.com/app/apikey

Replace your API Key in file: getRole.py on line no. 15

### Executing the Code:
```
python getRole.py
```
```
For Recruiter Route: Type 1
For Candidate Route: Type 2
```


