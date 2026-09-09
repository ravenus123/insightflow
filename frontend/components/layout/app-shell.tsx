import Link from "next/link";

export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="shell">
      <aside className="sidebar">
        <div className="brand">InsightFlow</div>
        <nav className="nav">
          <Link href="/">Overview</Link>
          <Link href="/upload">Datasets</Link>
          <Link href="/dashboard">Dashboard</Link>
          <a href="#">Reports <span className="badge">Soon</span></a>
          <a href="#">Settings <span className="badge">Soon</span></a>
        </nav>
      </aside>
      <main className="main">
        <div className="topbar">
          <div className="eyebrow">Demo Workspace</div>
          <div className="badge">V0.1 Wireframe</div>
        </div>
        <div className="content">{children}</div>
      </main>
    </div>
  );
}
