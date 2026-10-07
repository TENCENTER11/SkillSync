function SkillBar({ name, score, level }) {
  return (
    <div className="skill-row">

      <div className="skill-row-top">
        <div>
          <span className="skill-name">{name}</span>
          <span className="skill-level">{level}</span>
        </div>

        <strong>{score}%</strong>
      </div>

      <div className="progress-track">
        <div
          className="progress-fill"
          style={{ width: `${score}%` }}
        />
      </div>

    </div>
  );
}

export default SkillBar;