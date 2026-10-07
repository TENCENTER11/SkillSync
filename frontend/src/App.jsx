import { useState } from "react";

import {
  BarChart3,
  Map,
  Target,
  Home as HomeIcon,
  LogOut
} from "lucide-react";

import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Profile from "./pages/Profile";
import Dashboard from "./pages/Dashboard";
import SkillGap from "./pages/SkillGap";
import RoadmapPage from "./pages/RoadmapPage";

import { analyzeProfile } from "./services/api";

import "./App.css";

function App() {
  const [page, setPage] = useState("home");
  const [careerData, setCareerData] = useState(null);
  const [loading, setLoading] = useState(false);

  const startProfile = () => {
    setPage("profile");
    window.scrollTo(0, 0);
  };

  const analyze = async (profile) => {
    setLoading(true);

    const result = await analyzeProfile(profile);

    setCareerData({
      ...result,
      targetRole: profile.targetRole
    });

    setLoading(false);
    setPage("dashboard");
    window.scrollTo(0, 0);
  };

  const navigate = (nextPage) => {
    setPage(nextPage);
    window.scrollTo(0, 0);
  };

  if (loading) {
    return (
      <div className="loading-screen">
        <div className="loading-orb">
          <BarChart3 size={30} />
        </div>

        <h2>Building your Career Twin...</h2>

        <p>
          Analyzing your skills and career trajectory
        </p>

        <div className="loading-bar">
          <div />
        </div>
      </div>
    );
  }

  return (
    <div className="app">
      <Navbar
        onDashboard={() =>
          careerData ? navigate("dashboard") : startProfile()
        }
      />

      {careerData && page !== "home" && (
        <aside className="side-nav">
          <button
            className={page === "dashboard" ? "active" : ""}
            onClick={() => navigate("dashboard")}
          >
            <BarChart3 size={18} />
            Overview
          </button>

          <button
            className={page === "skillgap" ? "active" : ""}
            onClick={() => navigate("skillgap")}
          >
            <Target size={18} />
            Skill Gaps
          </button>

          <button
            className={page === "roadmap" ? "active" : ""}
            onClick={() => navigate("roadmap")}
          >
            <Map size={18} />
            Roadmap
          </button>

          <div className="side-divider" />

          <button onClick={() => navigate("home")}>
            <HomeIcon size={18} />
            Home
          </button>

          <button
            onClick={() => {
              setCareerData(null);
              setPage("home");
            }}
          >
            <LogOut size={18} />
            Start over
          </button>
        </aside>
      )}

      <main
        className={
          careerData && page !== "home" ? "with-sidebar" : ""
        }
      >
        {page === "home" && (
          <Home onStart={startProfile} />
        )}

        {page === "profile" && (
          <Profile onAnalyze={analyze} />
        )}

        {page === "dashboard" && careerData && (
          <Dashboard data={careerData} />
        )}

        {page === "skillgap" && careerData && (
          <SkillGap data={careerData} />
        )}

        {page === "roadmap" && careerData && (
          <RoadmapPage data={careerData} />
        )}
      </main>
    </div>
  );
}

export default App;