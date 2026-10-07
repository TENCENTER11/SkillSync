import { careerData } from "../data/mockData";

export const analyzeProfile = async (profile) => {
  // MOCK API FOR NOW
  // Later Member 1's backend will replace this.

  await new Promise((resolve) => setTimeout(resolve, 1200));

  return {
    ...careerData,
    profile
  };
};