const API_BASE_URL = "http://127.0.0.1:8000";

export const analyzeProfile = async (profile) => {
  const formData = new FormData();

  formData.append("file", profile.resume);
  formData.append("target_role", profile.targetRole);

  const response = await fetch(
    `${API_BASE_URL}/api/career/analyze`,
    {
      method: "POST",
      body: formData,
    }
  );

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));

    throw new Error(
      errorData.detail || "Career analysis failed"
    );
  }

  const data = await response.json();

  console.log("REAL BACKEND RESPONSE:", data);

  return {
    profile: {
      name: data.candidate?.name || "Unknown",
      education: data.candidate?.education || [],
      skills: data.candidate?.skills || [],
      experience: data.candidate?.experience || [],
      projects: data.candidate?.projects || [],
    },

    targetRole: data.target_role,

    matchScore: data.match_score,

    skills: (data.candidate?.skills || []).map((skill) => ({
      name: skill,
      score: 100,
      level: "Detected",
    })),

    skillGaps: (data.skill_gaps || []).map((gap) => ({
      name: gap.skill,
      priority: gap.priority,
      progress: 0,
      reason: gap.reason,
    })),

    roadmap: (data.roadmap || []).map((step) => ({
      week: `Step ${step.step}`,
      title: step.skill,
      description: step.objective,
      skills: [step.skill],
      status:
        step.priority === "High"
          ? "Priority"
          : step.priority === "Medium"
          ? "Next"
          : "Upcoming",
    })),

    recommendedProjects: [],
  };
};