from collections import defaultdict


class SkillGraph:
    """
    Represents relationships between skills.

    For the initial MVP, relationships can be loaded
    manually. Later, ESCO skill relationships will be used.
    """

    def __init__(self):
        self.graph = defaultdict(set)

    def add_relationship(
        self,
        skill_a: str,
        skill_b: str
    ):
        """
        Create a two-way relationship between two skills.
        """

        self.graph[skill_a].add(skill_b)
        self.graph[skill_b].add(skill_a)

    def add_relationships(
        self,
        relationships: list[tuple[str, str]]
    ):
        """
        Add multiple skill relationships.
        """

        for skill_a, skill_b in relationships:
            self.add_relationship(skill_a, skill_b)

    def get_related_skills(
        self,
        skill: str
    ) -> list[str]:
        """
        Return skills related to a given skill.
        """

        return sorted(self.graph.get(skill, set()))

    def get_all_relationships(self):
        """
        Return the complete skill graph.
        """

        return {
            skill: sorted(related)
            for skill, related in self.graph.items()
        }


# Temporary relationships for the MVP.
# These will later come from ESCO.

DEFAULT_RELATIONSHIPS = [
    ("Python", "Machine Learning"),
    ("Python", "Pandas"),
    ("Python", "NumPy"),
    ("Machine Learning", "Scikit-learn"),
    ("Machine Learning", "Deep Learning"),
    ("Machine Learning", "Statistics"),
    ("Deep Learning", "TensorFlow"),
    ("Deep Learning", "PyTorch"),
    ("Machine Learning", "Natural Language Processing"),
    ("Machine Learning", "Computer Vision"),
    ("Python", "FastAPI"),
    ("SQL", "PostgreSQL"),
    ("SQL", "MySQL"),
    ("Docker", "Kubernetes"),
    ("Git", "GitHub"),
    ("Data Structures", "Algorithms"),
    ("Algorithms", "C++"),
]


skill_graph = SkillGraph()

skill_graph.add_relationships(DEFAULT_RELATIONSHIPS)