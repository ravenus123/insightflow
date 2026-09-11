import Link from "next/link";
import { MoreHorizontal, Plus, Search, SlidersHorizontal } from "lucide-react";
import { PageHeader } from "@/components/ui/page-header";

const projects=[
  {name:"Retail Sales",desc:"Q1 sales performance and customer mix",quality:94,revenue:"€184.3k",updated:"2 min ago",tone:1},
  {name:"Subscription Revenue",desc:"MRR, retention and plan performance",quality:91,revenue:"€72.8k",updated:"Yesterday",tone:2},
  {name:"Wholesale Orders",desc:"Regional performance and top accounts",quality:88,revenue:"€311.4k",updated:"2 days ago",tone:3},
  {name:"Marketplace GMV",desc:"Channel and category contribution",quality:96,revenue:"€892.1k",updated:"4 days ago",tone:4},
  {name:"Store Performance",desc:"Location-level revenue and basket size",quality:84,revenue:"€425.6k",updated:"1 week ago",tone:5},
];
export default function ProjectsPage(){return <><PageHeader eyebrow="Library" title="Projects" description="Your analytics workspaces, datasets and decision history." actions={<Link className="button primary" href="/upload"><Plus size={16}/> New project</Link>}/><div className="toolbar glass-card"><div className="toolbar-search"><Search size={16}/><input placeholder="Search projects…"/></div><button className="button glass"><SlidersHorizontal size={15}/> Filter</button><span className="toolbar-count">5 projects</span></div><div className="project-library">{projects.map((p)=> <article className="library-card glass-card glass-interactive" key={p.name}><div className={`library-art art-${p.tone}`}><div className="library-orbit"/><span>{p.name.split(' ').map(v=>v[0]).join('')}</span><button className="icon-button"><MoreHorizontal size={17}/></button></div><div className="library-body"><div><h3>{p.name}</h3><p>{p.desc}</p></div><div className="library-stats"><span><small>Revenue</small>{p.revenue}</span><span><small>Quality</small>{p.quality}<em>/100</em></span></div><div className="library-foot"><span>Updated {p.updated}</span><Link href="/dashboard">Open project →</Link></div></div></article>)}</div></>}
