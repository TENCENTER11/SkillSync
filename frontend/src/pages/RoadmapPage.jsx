import { BookOpen, ExternalLink, Rocket } from "lucide-react";
import Roadmap from "../components/Roadmap";

function RoadmapPage({ data }) {

  return (
    <div className="dashboard-page">

      <div className="page-intro">

        <div className="eyebrow">
          <Rocket size={15} />
          PERSONALIZED LEARNING PATH
        </div>

        <h1>Your path to {data.targetRole}.</h1>

        <p>
          A focused roadmap generated from your current skills
          and career goal.
        </p>

      </div>


      <div className="roadmap-top-card">

        <div>
          <span>ESTIMATED JOURNEY</span>
          <strong>10 Weeks</strong>
        </div>

        <div>
          <span>SKILLS TO BUILD</span>
          <strong>{data.skillGaps.length}</strong>
        </div>

        <div>
          <span>PROJECTS</span>
          <strong>{data.recommendedProjects.length}</strong>
        </div>

      </div>


      <Roadmap roadmap={data.roadmap} />


      <div className="projects-section">

        <div className="section-heading-row">

          <div>
            <span>PORTFOLIO</span>
            <h2>Projects to prove your skills</h2>
          </div>

        </div>

        <div className="project-grid">

          {data.recommendedProjects.map((project) => (
            <div className="project-card" key={project}>

              <div className="project-icon">
                <BookOpen size={19} />
              </div>

              <div>
                <h3>{project}</h3>
                <p>
                  Recommended based on your career target.
                </p>
              </div>

              <ExternalLink size={17} />

            </div>
          ))}

        </div>

      </div>

    </div>
  );
}

export default RoadmapPage;