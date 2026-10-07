import { useState } from "react";

import {
  ArrowRight,
  Brain,
  CheckCircle2,
  ChevronRight,
  Sparkles,
  SlidersHorizontal
} from "lucide-react";

import CareerCard from "../components/CareerCard";
import SkillBar from "../components/SkillBar";
import SkillCard from "../components/SkillCard";
import Roadmap from "../components/Roadmap";

function Dashboard({ data }) {
  const [whatIf, setWhatIf] = useState(0);

  const simulatedScore = Math.min(
    98,
    data.matchScore + whatIf * 5
  );

  return (
    <div className="dashboard-page">
      <div className="dashboard-heading">
        <div>
          <span className="eyebrow-small">
            YOUR CAREER INTELLIGENCE
          </span>

          <h1>
            Welcome back
            {data.profile?.name
              ? `, ${data.profile.name.split(" ")[0]}`
              : ""}.
          </h1>

          <p>
            Here's what your Career Twin sees right now.
          </p>
        </div>

        <div className="ai-live">
          <span />
          AI analysis complete
        </div>
      </div>

      <CareerCard career={data} />

      <div className="dashboard-grid">
        <section className="dashboard-panel">
          <div className="panel-header">
            <div>
              <span>01</span>
              <h2>Your skill profile</h2>
            </div>

            <Brain size={21} />
          </div>

          <div className="skills-list">
            {data.skills.map((skill) => (
              <SkillBar
                key={skill.name}
                {...skill}
              />
            ))}
          </div>
        </section>

        <section className="dashboard-panel what-if-panel">
          <div className="panel-header">
            <div>
              <span>02</span>
              <h2>What if?</h2>
            </div>

            <SlidersHorizontal size={21} />
          </div>

          <p className="panel-description">
            Simulate what happens if you strengthen your weakest
            skills.
          </p>

          <div className="what-if-score">
            <div>
              <span>Current match</span>
              <strong>{data.matchScore}%</strong>
            </div>

            <ArrowRight />

            <div className="simulated">
              <span>Simulated</span>
              <strong>{simulatedScore}%</strong>
            </div>
          </div>

          <div className="slider-area">
            <label>
              Skills improved
              <strong>+{whatIf * 5}%</strong>
            </label>

            <input
              type="range"
              min="0"
              max="4"
              value={whatIf}
              onChange={(e) =>
                setWhatIf(Number(e.target.value))
              }
            />
          </div>

          <div className="simulation-result">
            <CheckCircle2 size={18} />

            {whatIf === 0
              ? "Move the slider to explore your potential."
              : `Improving ${whatIf} skill${
                  whatIf > 1 ? "s" : ""
                } could significantly increase your career match.`}
          </div>
        </section>
      </div>

      <section className="section-block">
        <div className="section-heading-row">
          <div>
            <span>03</span>
            <h2>Priority skill gaps</h2>
          </div>

          <button>
            View all
            <ChevronRight size={16} />
          </button>
        </div>

        <div className="gap-grid">
          {data.skillGaps.slice(0, 3).map((skill) => (
            <SkillCard
              key={skill.name}
              skill={skill}
            />
          ))}
        </div>
      </section>

      <section className="section-block roadmap-section">
        <div className="section-heading-row">
          <div>
            <span>04</span>
            <h2>Your personalized roadmap</h2>
          </div>

          <div className="roadmap-duration">
            <Sparkles size={15} />
            10 week plan
          </div>
        </div>

        <Roadmap roadmap={data.roadmap} />
      </section>
    </div>
  );
}

export default Dashboard;