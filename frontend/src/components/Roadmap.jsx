import { CheckCircle2, Circle, LockKeyhole } from "lucide-react";

function Roadmap({ roadmap }) {
  return (
    <div className="roadmap">

      {roadmap.map((item, index) => {

        const current = item.status === "Current";
        const completed = index === 0;

        return (
          <div className="roadmap-item" key={item.week}>

            <div className="timeline">

              <div className={`timeline-dot ${current ? "active" : ""}`}>
                {completed ? (
                  <CheckCircle2 size={17} />
                ) : item.status === "Next" ? (
                  <Circle size={15} />
                ) : (
                  <LockKeyhole size={14} />
                )}
              </div>

              {index !== roadmap.length - 1 && (
                <div className="timeline-line" />
              )}

            </div>

            <div className="roadmap-content">

              <div className="roadmap-meta">
                <span>{item.week} WEEKS</span>
                <span className={`roadmap-status ${item.status.toLowerCase()}`}>
                  {item.status}
                </span>
              </div>

              <h3>{item.title}</h3>

              <p>{item.description}</p>

              <div className="roadmap-tags">
                {item.skills.map((skill) => (
                  <span key={skill}>{skill}</span>
                ))}
              </div>

            </div>

          </div>
        );
      })}

    </div>
  );
}

export default Roadmap;