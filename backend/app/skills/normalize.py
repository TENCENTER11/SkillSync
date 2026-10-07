import re

from app.skills.taxonomy import SKILL_TAXONOMY


def normalize_skill(skill: str) -> str | None:
    """
    Convert a skill/alias into its canonical skill name.
    """

    skill = skill.strip().lower()

    if not skill:
        return None

    return SKILL_TAXONOMY.get(skill)


def normalize_skills(skills: list[str]) -> list[str]:
    """
    Normalize a list of skills and remove duplicates.
    """

    normalized = []

    for skill in skills:
        canonical = normalize_skill(skill)

        if canonical and canonical not in normalized:
            normalized.append(canonical)

    return normalized


def detect_skills(text: str) -> list[str]:
    """
    Detect known skills from resume text.
    """

    text_lower = text.lower()

    detected = []

    # Sort by length so that
    # 'machine learning' is checked before 'ml'
    skills = sorted(
        SKILL_TAXONOMY.keys(),
        key=len,
        reverse=True
    )

    for skill in skills:

        # Escape special regex characters
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text_lower):

            canonical = SKILL_TAXONOMY[skill]

            if canonical not in detected:
                detected.append(canonical)

    return detected