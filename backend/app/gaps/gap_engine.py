from app.skills.graph import skill_graph


def calculate_skill_priority(
    skill: str,
    required_skills: list[str],
    candidate_skills: list[str]
) -> str:
    """
    Determine the priority of a missing skill.

    High:
        Skill is directly required and has strong relationships
        with other required skills.

    Medium:
        Skill is required but has fewer relationships.

    Low:
        Skill is useful but less connected to the target role.
    """

    related_skills = skill_graph.get_related_skills(skill)

    required_connections = sum(
        1 for related in related_skills
        if related in required_skills
    )

    if required_connections >= 2:
        return "High"

    if required_connections >= 1:
        return "Medium"

    return "Low"


def generate_skill_gaps(
    candidate_skills: list[str],
    required_skills: list[str]
) -> list[dict]:
    """
    Generate prioritized skill gaps for a candidate.
    """

    candidate_set = set(candidate_skills)

    missing_skills = [
        skill
        for skill in required_skills
        if skill not in candidate_set
    ]

    gaps = []

    for skill in missing_skills:
        priority = calculate_skill_priority(
            skill,
            required_skills,
            candidate_skills
        )

        gaps.append({
            "skill": skill,
            "priority": priority,
            "reason": f"{skill} is required for the target career."
        })

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    gaps.sort(key=lambda x: priority_order[x["priority"]])

    return gaps