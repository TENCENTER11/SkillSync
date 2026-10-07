export const careerData = {
  targetRole: "AI / ML Engineer",
  matchScore: 78,

  summary:
    "You have a strong programming foundation and are building the right skills for an AI/ML career. Your biggest opportunities are advanced machine learning, deployment, and data engineering.",

  skills: [
    { name: "Python", score: 88, level: "Strong" },
    { name: "C++", score: 76, level: "Strong" },
    { name: "Machine Learning", score: 64, level: "Growing" },
    { name: "SQL", score: 58, level: "Growing" },
    { name: "Statistics", score: 52, level: "Developing" },
    { name: "Deep Learning", score: 38, level: "Beginner" }
  ],

  skillGaps: [
    {
      name: "Deep Learning",
      priority: "High",
      progress: 38,
      reason: "Frequently required for modern AI/ML roles."
    },
    {
      name: "MLOps",
      priority: "High",
      progress: 24,
      reason: "Important for deploying models into production."
    },
    {
      name: "Advanced SQL",
      priority: "Medium",
      progress: 58,
      reason: "Improves your ability to work with real-world datasets."
    },
    {
      name: "Statistics",
      priority: "Medium",
      progress: 52,
      reason: "Core foundation for reliable ML decision making."
    }
  ],

  roadmap: [
    {
      week: "01–02",
      title: "Strengthen Python & SQL",
      description:
        "Master data manipulation, SQL queries, joins and analytical workflows.",
      skills: ["Python", "SQL"],
      status: "Current"
    },
    {
      week: "03–04",
      title: "Machine Learning Foundations",
      description:
        "Build strong foundations in supervised and unsupervised learning.",
      skills: ["Scikit-learn", "Regression", "Classification"],
      status: "Next"
    },
    {
      week: "05–07",
      title: "Deep Learning",
      description:
        "Learn neural networks and build your first deep learning projects.",
      skills: ["PyTorch", "Neural Networks", "CNNs"],
      status: "Upcoming"
    },
    {
      week: "08–10",
      title: "Deploy AI Systems",
      description:
        "Learn APIs, Docker and deployment to turn models into real products.",
      skills: ["FastAPI", "Docker", "MLOps"],
      status: "Upcoming"
    }
  ],

  recommendedProjects: [
    "AI Resume Analyzer",
    "Customer Churn Prediction",
    "RAG-based Career Assistant"
  ]
};