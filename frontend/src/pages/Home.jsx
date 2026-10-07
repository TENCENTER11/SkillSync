import {
  ArrowRight,
  Brain,
  Target,
  TrendingUp,
  Sparkles,
  ShieldCheck,
  Zap
} from "lucide-react";

function Home({ onStart }) {
  return (
    <div>

      <section className="hero">

        <div className="hero-content">

          <div className="eyebrow">
            <Sparkles size={15} />
            AI-POWERED CAREER INTELLIGENCE
          </div>

          <h1>
            Your career.
            <br />
            <span>Your AI twin.</span>
          </h1>

          <p className="hero-description">
            SkillSync analyzes your skills, understands where you
            want to go, and creates a personalized path to get you
            there.
          </p>

          <div className="hero-buttons">

            <button className="primary-button" onClick={onStart}>
              Build My Career Twin
              <ArrowRight size={18} />
            </button>

            <button className="secondary-button">
              See how it works
            </button>

          </div>

          <div className="hero-trust">
            <ShieldCheck size={15} />
            Built around your skills, goals and potential
          </div>

        </div>


        <div className="hero-visual">

          <div className="hero-glow" />

          <div className="twin-card">

            <div className="twin-card-header">

              <div>
                <span>CAREER TWIN</span>
                <h3>Future Profile</h3>
              </div>

              <div className="live-status">
                <span />
                AI Active
              </div>

            </div>


            <div className="twin-role">

              <div className="role-icon">
                <Brain size={24} />
              </div>

              <div>
                <small>Target role</small>
                <h2>AI / ML Engineer</h2>
              </div>

            </div>


            <div className="twin-match">

              <div className="big-match">
                <div>
                  <strong>78</strong>
                  <small>%</small>
                </div>

                <span>Match</span>
              </div>

              <div className="match-copy">
                <h4>You're on track.</h4>

                <p>
                  Your strongest advantage is your programming
                  foundation.
                </p>
              </div>

            </div>


            <div className="twin-mini-grid">

              <div>
                <Target />
                <strong>12</strong>
                <span>Skills</span>
              </div>

              <div>
                <TrendingUp />
                <strong>4</strong>
                <span>Skill gaps</span>
              </div>

              <div>
                <Zap />
                <strong>10</strong>
                <span>Weeks</span>
              </div>

            </div>

          </div>

        </div>

      </section>


      <section className="feature-section">

        <div className="section-title">

          <span>ONE INTELLIGENT WORKSPACE</span>

          <h2>
            Know where you are.
            <br />
            Know where you're going.
          </h2>

        </div>


        <div className="feature-grid">

          <div className="feature-card">
            <Brain />
            <h3>Career Twin</h3>
            <p>
              Build a dynamic AI representation of your current
              skills, experience and career potential.
            </p>
          </div>

          <div className="feature-card">
            <Target />
            <h3>Skill Gap Intelligence</h3>
            <p>
              Identify the exact skills you need to develop for
              your target career.
            </p>
          </div>

          <div className="feature-card">
            <TrendingUp />
            <h3>Adaptive Roadmap</h3>
            <p>
              Follow a personalized learning roadmap instead of
              randomly collecting courses.
            </p>
          </div>

        </div>

      </section>

    </div>
  );
}

export default Home;