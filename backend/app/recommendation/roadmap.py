def generate_roadmap(skill_gaps: list[dict]) -> list[dict]:
    """
    Generate a personalized learning roadmap from prioritized skill gaps.
    """

    roadmap = []

    learning_actions = {
        "Statistics": {
            "objective": "Build a strong foundation in statistics for machine learning.",
            "action": "Study probability, distributions, hypothesis testing, correlation and regression."
        },
        "Scikit-learn": {
            "objective": "Learn practical machine learning implementation.",
            "action": "Build classification and regression models using Scikit-learn."
        },
        "Data Structures": {
            "objective": "Strengthen problem-solving and technical interview skills.",
            "action": "Practice arrays, linked lists, stacks, queues, trees and algorithms."
        },
        "Docker": {
            "objective": "Learn how to package and deploy applications.",
            "action": "Containerize a Python/FastAPI machine-learning application."
        },
        "Python": {
            "objective": "Strengthen Python programming for AI development.",
            "action": "Practice Python programming, data handling and object-oriented programming."
        },
        "SQL": {
            "objective": "Improve data querying and database skills.",
            "action": "Practice joins, aggregation, subqueries and analytical SQL."
        },
        "Machine Learning": {
            "objective": "Build practical machine-learning knowledge.",
            "action": "Study supervised learning, evaluation metrics and model selection."
        },
        "Deep Learning": {
            "objective": "Develop neural-network and deep-learning skills.",
            "action": "Build projects using PyTorch or TensorFlow."
        }
    }

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    sorted_gaps = sorted(
        skill_gaps,
        key=lambda gap: priority_order.get(gap.get("priority"), 4)
    )

    for index, gap in enumerate(sorted_gaps, start=1):
        skill = gap["skill"]
        priority = gap["priority"]

        action = learning_actions.get(
            skill,
            {
                "objective": f"Develop {skill} skills for the target career.",
                "action": f"Learn {skill} through structured study and a practical project."
            }
        )

        roadmap.append({
            "step": index,
            "skill": skill,
            "priority": priority,
            "objective": action["objective"],
            "recommended_action": action["action"]
        })

    return roadmap