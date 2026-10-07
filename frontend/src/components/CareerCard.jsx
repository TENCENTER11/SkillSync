import { Brain, Target, TrendingUp } from "lucide-react";

function CareerCard({ career }) {
  return (
    <div className="career-dashboard-card">

      <div className="career-card-top">

        <div>
          <span className="eyebrow-small">
            YOUR CAREER TWIN
          </span>

          <h2>{career.targetRole}</h2>

          <p>{career.summary}</p>
        </div>

        <div className="career-match">
          <div className="match-ring">
            <strong>{career.matchScore}%</strong>
          </div>

          <span>Career Match</span>
        </div>

      </div>

      <div className="career-insights">

        <div>
          <Brain size={20} />
          <span>AI Profile</span>
          <strong>Active</strong>
        </div>

        <div>
          <Target size={20} />
          <span>Skills Tracked</span>
          <strong>{career.skills.length}</strong>
        </div>

        <div>
          <TrendingUp size={20} />
          <span>Growth Potential</span>
          <strong>High</strong>
        </div>

      </div>

    </div>
  );
}

export default CareerCard;