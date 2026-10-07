from app.matching.embeddings import embedding_model


def calculate_skill_similarity(
    candidate_skill: str,
    required_skill: str
) -> float:
    """
    Calculate semantic similarity between
    a candidate skill and a required skill.
    """

    candidate_embedding = embedding_model.encode(
        candidate_skill
    )

    required_embedding = embedding_model.encode(
        required_skill
    )

    similarity = float(
        candidate_embedding @ required_embedding
    )

    return similarity


def match_skills(
    candidate_skills: list[str],
    required_skills: list[str],
    threshold: float = 0.55
) -> dict:
    """
    Match candidate skills against required skills
    using semantic similarity.
    """

    matched = []
    missing = []

    for required_skill in required_skills:

        best_match = None
        best_score = 0.0

        for candidate_skill in candidate_skills:

            score = calculate_skill_similarity(
                candidate_skill,
                required_skill
            )

            if score > best_score:
                best_score = score
                best_match = candidate_skill

        if best_score >= threshold:

            matched.append({
                "required_skill": required_skill,
                "candidate_skill": best_match,
                "similarity": round(best_score, 3)
            })

        else:

            missing.append({
                "skill": required_skill,
                "best_candidate_match": best_match,
                "similarity": round(best_score, 3)
            })

    return {
        "matched_skills": matched,
        "missing_skills": missing
    }


def calculate_match_score(
    candidate_skills: list[str],
    required_skills: list[str]
) -> float:
    """
    Calculate overall career compatibility score.
    """

    if not required_skills:
        return 0.0

    result = match_skills(
        candidate_skills,
        required_skills
    )

    matched_count = len(
        result["matched_skills"]
    )

    score = (
        matched_count /
        len(required_skills)
    ) * 100

    return round(score, 2)