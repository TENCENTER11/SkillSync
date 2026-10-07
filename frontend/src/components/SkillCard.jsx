import { AlertTriangle, ArrowUpRight } from "lucide-react";

function SkillCard({ skill }) {
  return (
    <div className="gap-card">

      <div className="gap-card-header">
        <div className="gap-icon">
          <AlertTriangle size={18} />
        </div>

        <div>
          <h3>{skill.name}</h3>

          <span className={`priority ${skill.priority.toLowerCase()}`}>
            {skill.priority} Priority
          </span>
        </div>

        <ArrowUpRight className="gap-arrow" size={18} />
      </div>

      <p>{skill.reason}</p>

      <div className="gap-progress">
        <div>
          <span>Current proficiency</span>
          <strong>{skill.progress}%</strong>
        </div>

        <div className="progress-track">
          <div
            className="progress-fill"
            style={{ width: `${skill.progress}%` }}
          />
        </div>
      </div>

    </div>
  );
}

export default SkillCard;