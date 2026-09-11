import Link from "next/link";
import { ArrowRight, BarChart3, Check, Database, UploadCloud } from "lucide-react";
import { AmbientBackground } from "@/components/ambient-background";
import { Logo } from "@/components/logo";

export default function LandingPage() {
  return (
    <div className="marketing-shell">
      <AmbientBackground />
      <header className="marketing-nav">
        <Logo />
        <nav><a href="#product">Product</a><a href="#workflow">Workflow</a><a href="#engineering">Engineering</a></nav>
        <div className="marketing-actions"><Link className="button ghost" href="/signin">Sign in</Link><Link className="button primary" href="/overview">Open demo <ArrowRight size={16}/></Link></div>
      </header>
      <main>
        <section className="hero">
          <div className="hero-copy reveal">
            <div className="hero-kicker">Business analytics without the spreadsheet sprawl</div>
            <h1>From raw rows to <span>clear decisions.</span></h1>
            <p>InsightFlow turns messy sales data into polished analytics, quality checks and clear business insights — without a spreadsheet maze.</p>
            <div className="hero-actions"><Link className="button primary large" href="/overview">Explore the demo <ArrowRight size={18}/></Link><Link className="button glass large" href="/upload"><UploadCloud size={18}/> Import a dataset</Link></div>
            <div className="hero-proof"><span><Check size={14}/> CSV & XLSX</span><span><Check size={14}/> Deterministic insights</span><span><Check size={14}/> No AI required</span></div>
          </div>
          <div className="hero-product-wrap reveal delay-2">
            <div className="hero-product glow-frame">
              <div className="window-bar"><div className="window-dots"><i/><i/><i/></div><span>Acme Analytics · Q1 Sales</span><div /></div>
              <div className="mini-dashboard">
                <div className="mini-side"><div className="mini-logo"/><span className="mini-nav active"/><span className="mini-nav"/><span className="mini-nav short"/><div className="mini-grow"/><span className="mini-nav short"/></div>
                <div className="mini-main">
                  <div className="mini-heading"><div><small>PERFORMANCE</small><strong>Sales overview</strong></div><span className="mini-pill">Q1 2026</span></div>
                  <div className="mini-metrics"><div><small>Revenue</small><strong>€184.3k</strong><em>+12.4%</em></div><div><small>Orders</small><strong>2,481</strong><em>+7.1%</em></div><div><small>Customers</small><strong>1,043</strong><em>+4.8%</em></div></div>
                  <div className="mini-chart-card"><div className="mini-chart-head"><span>Revenue trend</span><small>Jan — Mar</small></div><svg viewBox="0 0 620 180" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="area" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stopColor="#8d7bff" stopOpacity=".5"/><stop offset="100%" stopColor="#8d7bff" stopOpacity="0"/></linearGradient></defs><path className="mini-area" d="M0,150 C35,140 45,80 92,105 C128,125 140,62 190,72 C250,84 258,31 305,55 C350,78 372,122 414,90 C465,50 480,65 520,35 C557,8 580,38 620,18 L620,180 L0,180 Z"/><path className="mini-line" d="M0,150 C35,140 45,80 92,105 C128,125 140,62 190,72 C250,84 258,31 305,55 C350,78 372,122 414,90 C465,50 480,65 520,35 C557,8 580,38 620,18"/></svg></div>
                  <div className="mini-bottom"><div><small>Best category</small><strong>Electronics</strong><span className="mini-progress"><i style={{width:"78%"}}/></span></div><div><small>Data quality</small><strong>94 / 100</strong><span className="mini-progress"><i style={{width:"94%"}}/></span></div></div>
                </div>
              </div>
            </div>
            <div className="floating-card float-a"><div className="floating-icon"><BarChart3 size={18}/></div><div><small>Accessories</small><strong>+24.7% vs previous period</strong></div></div>
            <div className="floating-card float-b"><div className="floating-icon"><Database size={18}/></div><div><small>Data quality</small><strong>94 / 100 · 3 warnings</strong></div></div>
          </div>
        </section>
        <section id="product" className="marketing-section">
          <div className="section-heading"><div className="eyebrow"><span/>Made for real data</div><h2>One calm workflow from upload to answer.</h2><p>No visual noise. No mystery metrics. Every result traces back to your data.</p></div>
          <div className="feature-grid">
            <article className="feature-card"><div className="feature-icon"><UploadCloud/></div><h3>Structured ingestion</h3><p>Parse CSV/XLSX, inspect schema and map business meaning before any metric is calculated.</p></article>
            <article className="feature-card"><div className="feature-icon"><Database/></div><h3>Data quality first</h3><p>Surface duplicates, missing values, invalid dates and suspicious revenue before they reach a dashboard.</p></article>
            <article className="feature-card"><div className="feature-icon"><BarChart3/></div><h3>Traceable analytics</h3><p>Revenue, orders, customers, category mix and deterministic insights in one focused workspace.</p></article>
          </div>
        </section>
        <section id="workflow" className="workflow-section">
          <div className="workflow-line" />
          {[["01","Import","Drop sales data from the systems you already use."],["02","Map","Confirm what each source column means to the business."],["03","Validate","Catch quality issues before they distort the answer."],["04","Explore","Move from KPIs to trends, segments and exports."]].map(([n,t,d])=><article key={n}><span>{n}</span><h3>{t}</h3><p>{d}</p></article>)}
        </section>
      </main>
      <footer className="marketing-footer"><Logo/><p>Portfolio-grade analytics engineering, built end-to-end.</p><span>© 2026 InsightFlow</span></footer>
    </div>
  );
}
