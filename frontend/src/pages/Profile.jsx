import { useState } from "react";
import {
  ArrowRight,
  Upload,
  User,
  GraduationCap,
  Briefcase,
  Sparkles
} from "lucide-react";

function Profile({ onAnalyze }) {

  const [form, setForm] = useState({
    name: "",
    education: "",
    targetRole: "AI / ML Engineer",
    skills: "",
    experience: ""
  });

  const update = (field, value) => {
    setForm({
      ...form,
      [field]: value
    });
  };

  const submit = (e) => {
    e.preventDefault();

    onAnalyze({
      ...form,
      skills: form.skills
        .split(",")
        .map((skill) => skill.trim())
        .filter(Boolean)
    });
  };

  return (
    <div className="profile-page">

      <div className="profile-heading">

        <div className="eyebrow">
          <Sparkles size={15} />
          CREATE YOUR CAREER TWIN
        </div>

        <h1>Tell us about yourself.</h1>

        <p>
          Give SkillSync a little context. Our AI will turn it
          into your personalized career intelligence profile.
        </p>

      </div>


      <form className="profile-form" onSubmit={submit}>

        <div className="form-section">

          <div className="form-section-title">
            <User />
            <div>
              <h3>About you</h3>
              <p>Your basic profile information</p>
            </div>
          </div>

          <div className="form-grid">

            <label>
              Full name

              <input
                value={form.name}
                onChange={(e) => update("name", e.target.value)}
                placeholder="e.g. Alex Sharma"
                required
              />
            </label>

            <label>
              Education

              <input
                value={form.education}
                onChange={(e) =>
                  update("education", e.target.value)
                }
                placeholder="e.g. B.E. Computer Science"
                required
              />
            </label>

          </div>

        </div>


        <div className="form-section">

          <div className="form-section-title">
            <Briefcase />
            <div>
              <h3>Career direction</h3>
              <p>Where do you want your career to go?</p>
            </div>
          </div>

          <label>
            Target role

            <select
              value={form.targetRole}
              onChange={(e) =>
                update("targetRole", e.target.value)
              }
            >
              <option>AI / ML Engineer</option>
              <option>Data Scientist</option>
              <option>Software Engineer</option>
              <option>Data Analyst</option>
              <option>Product Manager</option>
            </select>
          </label>

        </div>


        <div className="form-section">

          <div className="form-section-title">
            <GraduationCap />
            <div>
              <h3>Your skills</h3>
              <p>Separate multiple skills with commas</p>
            </div>
          </div>

          <label>
            Current skills

            <input
              value={form.skills}
              onChange={(e) =>
                update("skills", e.target.value)
              }
              placeholder="Python, C++, SQL, Machine Learning"
              required
            />
          </label>

        </div>


        <div className="resume-upload">

          <div className="upload-icon">
            <Upload size={22} />
          </div>

          <div>
            <h3>Upload your resume</h3>
            <p>
              Optional for now — AI resume parsing will connect
              here later.
            </p>
          </div>

          <button
            type="button"
            className="upload-button"
          >
            Choose file
          </button>

        </div>


        <button className="analyze-button" type="submit">
          Analyze My Career
          <ArrowRight size={19} />
        </button>

      </form>

    </div>
  );
}

export default Profile;