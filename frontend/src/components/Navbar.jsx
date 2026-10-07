import { Brain, LayoutDashboard, Sparkles } from "lucide-react";

function Navbar({ onDashboard }) {
  return (
    <nav className="navbar">
      <div className="logo">
        <div className="logo-icon">
          <Brain size={20} />
        </div>

        <span>SkillSync</span>

        <span className="ai-badge">AI</span>
      </div>

      <div className="nav-links">
        <button onClick={onDashboard}>
          <LayoutDashboard size={16} />
          Dashboard
        </button>

        <div className="nav-ai">
          <Sparkles size={14} />
          Career Intelligence
        </div>
      </div>
    </nav>
  );
}

export default Navbar;