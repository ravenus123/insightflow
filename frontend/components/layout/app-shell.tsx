"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { BarChart3, Bell, ChevronDown, CircleHelp, Database, FileBarChart, FolderKanban, Globe2, LayoutDashboard, Plus, Search, Settings2, UploadCloud } from "lucide-react";
import { Logo } from "@/components/logo";
import { AmbientBackground } from "@/components/ambient-background";

const items = [
  ["/overview", "Overview", LayoutDashboard],
  ["/projects", "Projects", FolderKanban],
  ["/upload", "Import data", UploadCloud],
  ["/dashboard", "Analytics", BarChart3],
  ["/reports", "Reports", FileBarChart],
  ["/settings", "Settings", Settings2],
] as const;

export function AppShell({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  return (
    <div className="app-frame">
      <AmbientBackground />
      <aside className="side-panel">
        <div className="side-head"><Link href="/overview"><Logo /></Link><button className="icon-button compact" aria-label="Create new"><Plus size={16}/></button></div>
        <button className="workspace-switcher">
          <div className="workspace-avatar">A</div>
          <div><span>Workspace</span><strong>Acme Analytics</strong></div>
          <ChevronDown size={15}/>
        </button>
        <nav className="side-nav">
          <div className="nav-label">Workspace</div>
          {items.map(([href,label,Icon]) => {
            const active = pathname === href || (href !== "/overview" && pathname.startsWith(href));
            return <Link key={href} href={href} className={`nav-item ${active ? "active" : ""}`}><Icon size={18}/><span>{label}</span>{active && <i />}</Link>;
          })}
        </nav>
        <div className="side-spacer" />
        <div className="storage-card">
          <div className="storage-icon"><Database size={17}/></div>
          <div className="storage-copy"><strong>Data storage</strong><span>1.8 GB of 10 GB</span></div>
          <div className="storage-track"><span style={{width:"18%"}} /></div>
        </div>
        <div className="side-bottom">
          <Link href="/" className="nav-item"><Globe2 size={18}/><span>Product site</span></Link>
          <a href="https://github.com/ravenus123/insightflow" target="_blank" rel="noreferrer" className="nav-item"><CircleHelp size={18}/><span>Documentation</span></a>
        </div>
      </aside>
      <main className="workspace-main">
        <header className="top-panel">
          <div className="command-search"><Search size={16}/><span>Search metrics, datasets, reports…</span><kbd>⌘ K</kbd></div>
          <div className="top-actions">
            <button className="icon-button" aria-label="Notifications"><Bell size={18}/><i className="notify-dot"/></button>
            <button className="profile-pill"><span className="avatar">AV</span><span className="profile-copy"><strong>Adam V.</strong><small>Owner</small></span><ChevronDown size={14}/></button>
          </div>
        </header>
        <div className="workspace-content">{children}</div>
      </main>
    </div>
  );
}
