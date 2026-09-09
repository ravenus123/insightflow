import Link from "next/link";
import { PageHeader } from "@/components/ui/page-header";

export default function HomePage() {
  return (
    <>
      <PageHeader title="InsightFlow" description="Turn raw sales data into clear business decisions." />
      <div className="grid grid-2">
        <div className="card card-pad">
          <div className="eyebrow">Start here</div>
          <h2>Import a sales dataset</h2>
          <p style={{ color: "var(--muted)" }}>Upload a CSV, inspect the detected schema, confirm semantic column mappings and generate a dashboard.</p>
          <Link className="button primary" href="/upload">Upload dataset</Link>
        </div>
        <div className="card card-pad">
          <div className="eyebrow">Wireframe scope</div>
          <h2>V0.1</h2>
          <p style={{ color: "var(--muted)" }}>UI shell, upload, preview, semantic mapping and analytics dashboard. Visual styling comes after the design sheet.</p>
          <Link className="button" href="/dashboard">View dashboard wireframe</Link>
        </div>
      </div>
    </>
  );
}
