const analyze = async (profile) => {
  setLoading(true);

  try {
    const result = await analyzeProfile(profile);

    setCareerData({
      ...result,
      targetRole: profile.targetRole
    });

    setPage("dashboard");
    window.scrollTo(0, 0);

  } catch (error) {
    console.error("Career analysis failed:", error);

    alert(
      error.message ||
      "Something went wrong while analyzing your resume."
    );

  } finally {
    setLoading(false);
  }
};