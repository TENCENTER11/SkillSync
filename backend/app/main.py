from fastapi import FastAPI, UploadFile, File, HTTPException

from app.resume.parser import extract_text_from_pdf
from app.resume.extractor import extract_resume_information

from app.matching.matcher import match_skills, calculate_match_score
from app.matching.career_profiles import CAREER_PROFILES

from app.gaps.gap_engine import generate_skill_gaps
from fastapi.middleware.cors import CORSMiddleware
from app.recommendation.roadmap import generate_roadmap

app = FastAPI(
    title="SkillSync AI",
    description="AI-powered Career and Talent Intelligence API",
    version="0.1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "SkillSync AI API is running",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/api/resume/parse")
async def parse_resume(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF resumes are supported"
        )

    file_bytes = await file.read()

    text = extract_text_from_pdf(file_bytes)

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from PDF"
        )

    resume_data = extract_resume_information(text)

    return {
        "filename": file.filename,
        "resume": resume_data,
        "raw_text": text
    }

@app.post("/api/career/match")
def career_match(candidate_skills: list[str], target_role: str):
    if target_role not in CAREER_PROFILES:
        raise HTTPException(
            status_code=404,
            detail="Career profile not found"
        )

    required_skills = CAREER_PROFILES[target_role]

    result = match_skills(
        candidate_skills,
        required_skills
    )

    score = calculate_match_score(
        candidate_skills,
        required_skills
    )

    skill_gaps = generate_skill_gaps(
        candidate_skills,
        required_skills
    )

    roadmap = generate_roadmap(skill_gaps)

    return {
        "target_role": target_role,
        "match_score": score,
        "required_skills": required_skills,
        "matched_skills": result["matched_skills"],
        "missing_skills": result["missing_skills"],
        "skill_gaps": skill_gaps,
        "roadmap": roadmap
    }


@app.post("/api/career/analyze")
async def career_analyze(
    file: UploadFile = File(...),
    target_role: str = ""
):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF resumes are supported"
        )

    if target_role not in CAREER_PROFILES:
        raise HTTPException(
            status_code=404,
            detail="Career profile not found"
        )

    file_bytes = await file.read()

    # Extract resume text
    text = extract_text_from_pdf(file_bytes)

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from PDF"
        )

    # Extract candidate information
    resume_data = extract_resume_information(text)

    # Candidate skills extracted from resume
    candidate_skills = resume_data["skills"]

    # Required skills for selected career
    required_skills = CAREER_PROFILES[target_role]

    # Match skills
    result = match_skills(
        candidate_skills,
        required_skills
    )

    # Calculate match score
    score = calculate_match_score(
        candidate_skills,
        required_skills
    )

    # Generate skill gaps
    skill_gaps = generate_skill_gaps(
        candidate_skills,
        required_skills
    )

    # Generate roadmap
    roadmap = generate_roadmap(skill_gaps)

    return {
        "filename": file.filename,
        "candidate": resume_data,
        "target_role": target_role,
        "match_score": score,
        "required_skills": required_skills,
        "matched_skills": result["matched_skills"],
        "missing_skills": result["missing_skills"],
        "skill_gaps": skill_gaps,
        "roadmap": roadmap
    }