import { useState } from "react";

import {
  ArrowRight,
  Upload,
  Sparkles,
  FileText
} from "lucide-react";

function Profile({ onAnalyze }) {
  const [resume, setResume] = useState(null);
  const [targetRole, setTargetRole] = useState(
    "Machine Learning Engineer"
  );

  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    const file = e.target.files?.[0];

    if (!file) return;

    if (file.type !== "application/pdf") {
      setError("Please upload a PDF resume.");
      setResume(null);
      return;
    }

    setError("");
    setResume(file);
  };

  const submit = (e) => {
    e.preventDefault();

    if (!resume) {
      setError("Please upload your resume first.");
      return;
    }

    setError("");

    onAnalyze({
      resume,
      targetRole,
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
          Upload your resume and let SkillSync analyze your
          actual skills and career readiness.
        </p>

      </div>

      <form
        className="profile-form"
        onSubmit={submit}
      >

        <div className="form-section">

          <div className="form-section-title">
            <Sparkles />

            <div>
              <h3>Career direction</h3>

              <p>
                Select the career you want to analyze yourself against.
              </p>
            </div>
          </div>

          <label>
            Target role

            <select
              value={targetRole}
              onChange={(e) =>
                setTargetRole(e.target.value)
              }
            >
              <option>
                Machine Learning Engineer
              </option>

              <option>
                Data Scientist
              </option>

              <option>
                Backend Developer
              </option>

              <option>
                AI Engineer
              </option>
            </select>
          </label>

        </div>

        <div className="form-section">

          <div className="form-section-title">
            <FileText />

            <div>
              <h3>Upload your resume</h3>

              <p>
                SkillSync will extract your actual skills,
                education, projects and experience.
              </p>
            </div>
          </div>

          <div className="resume-upload">

            <div className="upload-icon">
              <Upload size={22} />
            </div>

            <div>
              <h3>
                {resume
                  ? resume.name
                  : "Choose your PDF resume"}
              </h3>

              <p>
                {resume
                  ? `${(resume.size / 1024).toFixed(1)} KB`
                  : "PDF files only"}
              </p>
            </div>

            <label className="upload-button">
              Choose file

              <input
                type="file"
                accept="application/pdf"
                onChange={handleFileChange}
                hidden
              />
            </label>

          </div>

        </div>

        {error && (
          <div className="form-error">
            {error}
          </div>
        )}

        <button
          className="analyze-button"
          type="submit"
        >
          Analyze My Career
          <ArrowRight size={19} />
        </button>

      </form>

    </div>
  );
}

export default Profile;