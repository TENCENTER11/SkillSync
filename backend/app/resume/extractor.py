import re
from app.skills.normalize import detect_skills

def clean_text(text: str) -> str:
    """Clean unnecessary spaces and blank lines."""

    text = text.replace("\r", "\n")

    lines = []

    for line in text.split("\n"):
        line = line.strip()

        if line:
            lines.append(line)

    return "\n".join(lines)


def extract_name(text: str) -> str:
    """Extract the likely candidate name from the beginning of the resume."""

    lines = text.split("\n")

    for line in lines[:10]:
        line = line.strip()

        if not line:
            continue

        # Ignore common resume headings
        if line.lower() in {
            "resume",
            "curriculum vitae",
            "cv",
            "profile",
            "summary",
        }:
            continue

        # Names generally don't contain many special characters
        if (
            len(line.split()) <= 5
            and not any(char.isdigit() for char in line)
            and "@" not in line
        ):
            return line

    return "Unknown"


def extract_section(text: str, section_names: list[str]) -> list[str]:
    """
    Extract lines belonging to a resume section.
    """

    lines = text.split("\n")

    start_index = None

    for i, line in enumerate(lines):
        normalized = line.lower().strip()

        if normalized in section_names:
            start_index = i + 1
            break

    if start_index is None:
        return []

    section = []

    common_sections = {
        "education",
        "skills",
        "technical skills",
        "projects",
        "experience",
        "work experience",
        "professional experience",
        "certifications",
        "achievements",
        "languages",
        "interests",
        "summary",
        "profile",
    }

    for line in lines[start_index:]:
        normalized = line.lower().strip()

        if normalized in common_sections:
            break

        if line.strip():
            section.append(line.strip())

    return section


def extract_resume_information(text: str) -> dict:
    """
    Convert raw resume text into structured information.
    """

    text = clean_text(text)
    detected_skills = detect_skills(text)

    education = extract_section(
        text,
        [
            "education",
            "academic background",
            "educational background",
        ],
    )

    skills = extract_section(
        text,
        [
            "skills",
            "technical skills",
            "technical skill",
            "skills & technologies",
        ],
    )

    projects = extract_section(
        text,
        [
            "projects",
            "academic projects",
            "personal projects",
        ],
    )

    experience = extract_section(
        text,
        [
            "experience",
            "work experience",
            "professional experience",
            "internship",
        ],
    )

    return {
        "name": extract_name(text),
        "education": education,
        "skills": detected_skills,
        "projects": projects,
        "experience": experience,
    }