import Link from "next/link";
import { ArrowRight, CheckCircle2, Clock3, Database, FileSpreadsheet, Plus, TrendingUp, UploadCloud } from "lucide-react";
import { PageHeader } from "@/components/ui/page-header";
import { GlassCard } from "@/components/ui/glass-card";
import { MetricCard } from "@/components/ui/metric-card";

export default function OverviewPage(){return <>
  <PageHeader eyebrow="Workspace" title="Good evening, Adam." description="Everything important across your analytics workspace, without the noise." actions={<Link href="/upload" className="button primary"><Plus size={16}/> New analysis</Link>}/>
  <div className="metric-grid reveal delay-1"><MetricCard label="Revenue" value="€184.3k" delta={12.4} helper="vs previous period" icon={<TrendingUp size={17}/>}/><MetricCard label="Datasets" value="06" delta={20} helper="2 updated this week" icon={<Database size={17}/>}/><MetricCard label="Data quality" value="94 / 100" delta={3.2} helper="workspace average" icon={<CheckCircle2 size={17}/>}/><MetricCard label="Reports" value="12" helper="last export 2h ago" icon={<FileSpreadsheet size={17}/>}/></div>
  <div className="overview-layout reveal delay-2">
    <GlassCard className="focus-card">
      <div className="card-heading"><div><div className="eyebrow"><span/>Continue where you left off</div><h2>Retail Sales · Q1 2026</h2><p>Clean dataset · 2,481 rows · refreshed today</p></div></div>
      <div className="focus-visual"><div className="focus-orb"><span>94</span><small>quality</small></div><div className="focus-copy"><strong>All critical mappings are confirmed.</strong><p>Three low-risk quality warnings remain and stay visible alongside the analytics.</p><div className="inline-stats"><span><small>Revenue</small>€184.3k</span><span><small>Orders</small>2,481</span><span><small>Customers</small>1,043</span></div></div></div>
      <div className="card-footer-actions"><Link href="/dashboard" className="button primary">Open analytics <ArrowRight size={16}/></Link><Link href="/quality" className="button glass">Review quality</Link></div>
    </GlassCard>
    <GlassCard className="activity-card">
      <div className="card-heading compact"><div><div className="eyebrow"><span/>Activity</div><h3>Recent changes</h3></div><button className="icon-button"><Clock3 size={17}/></button></div>
      <div className="activity-list">{[["Dataset imported","Retail Sales Q1","2 min ago",UploadCloud],["Quality scan completed","94 / 100 · 3 warnings","4 min ago",CheckCircle2],["Report exported","Executive overview.pdf","2 hours ago",FileSpreadsheet],["Dataset refreshed","Subscription Revenue","Yesterday",Database]].map(([t,s,time,I],i)=>{const Icon=I as typeof Database;return <div className="activity-row" key={i}><div className="activity-icon"><Icon size={16}/></div><div><strong>{t as string}</strong><span>{s as string}</span></div><time>{time as string}</time></div>})}</div>
    </GlassCard>
  </div>
  <div className="section-strip"><div><div className="eyebrow"><span/>Recent projects</div><h2>Pick up any analysis</h2></div><Link href="/projects">View all <ArrowRight size={15}/></Link></div>
  <div className="project-grid reveal delay-3">{[["Retail Sales","Q1 2026 performance","94","€184k"],["Subscription Revenue","MRR & churn tracking","91","€72k"],["Wholesale Orders","Regional mix","88","€311k"]].map((p,i)=><Link href="/dashboard" className="project-card glass-card glass-interactive" key={p[0]}><div className={`project-art art-${i+1}`}><span className="project-monogram">{p[0].split(' ').map(x=>x[0]).join('')}</span><div className="project-spark"><i/><i/><i/><i/><i/></div></div><div className="project-body"><div><h3>{p[0]}</h3><p>{p[1]}</p></div><div className="project-meta"><span><small>Quality</small>{p[2]}</span><span><small>Revenue</small>{p[3]}</span></div></div></Link>)}</div>
</>}
