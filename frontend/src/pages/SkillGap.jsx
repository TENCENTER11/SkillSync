import SkillCard from "../components/SkillCard";
import { Target, Sparkles } from "lucide-react";

function SkillGap({ data }) {
  return (
    <div className="dashboard-page">

      <div className="page-intro">

        <div className="eyebrow">
          <Target size={15} />
          SKILL GAP INTELLIGENCE
        </div>

        <h1>Know exactly what to improve.</h1>

        <p>
          SkillSync compares your current profile against your
          target role and identifies the highest-impact gaps.
        </p>

      </div>

      <div className="gap-summary">

        <div>
          <span>Total gaps</span>
          <strong>{data.skillGaps.length}</strong>
        </div>

        <div>
          <span>High priority</span>
          <strong>
            {data.skillGaps.filter(
              (skill) => skill.priority === "High"
            ).length}
          </strong>
        </div>

        <div>
          <span>Target role</span>
          <strong>{data.targetRole}</strong>
        </div>

      </div>

      <div className="gap-page-grid">

        {data.skillGaps.map((skill) => (
          <SkillCard
            key={skill.name}
            skill={skill}
          />
        ))}

      </div>

      <div className="ai-insight">

        <Sparkles />

        <div>
          <strong>AI recommendation</strong>

          <p>
            Focus on Deep Learning and MLOps first. Together,
            these skills provide the highest expected improvement
            toward your target role.
          </p>
        </div>

      </div>

    </div>
  );
}

export default SkillGap;