from fastapi import FastAPI, UploadFile, File, HTTPException

from app.resume.parser import extract_text_from_pdf
from app.resume.extractor import extract_resume_information

from app.matching.matcher import match_skills, calculate_match_score
from app.matching.career_profiles import CAREER_PROFILES


app = FastAPI(
    title="SkillSync AI",
    description="AI-powered Career and Talent Intelligence API",
    version="0.1.0"
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
def career_match(
    candidate_skills: list[str],
    target_role: str
):

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

    return {
        "target_role": target_role,
        "match_score": score,
        "required_skills": required_skills,
        **result
    }