"use client";

import Link from "next/link";
import { useState } from "react";
import { PageHeader } from "@/components/ui/page-header";

export default function UploadPage() {
  const [filename, setFilename] = useState<string | null>(null);
  return (
    <>
      <PageHeader title="Import dataset" description="Bring a sales CSV into InsightFlow." />
      <div className="dropzone">
        <div className="dropzone-inner">
          <div className="eyebrow">CSV import</div>
          <h2>{filename ?? "Drop your dataset here"}</h2>
          <p>Wireframe upload flow. Maximum V0.1 file size: 25 MB.</p>
          <label className="button primary">
            Choose file
            <input hidden type="file" accept=".csv,text/csv" onChange={(e) => setFilename(e.target.files?.[0]?.name ?? null)} />
          </label>
          {filename && <div style={{ marginTop: 14 }}><Link className="button" href="/preview">Continue to preview</Link></div>}
        </div>
      </div>
      <div style={{ height: 16 }} />
      <div className="notice">Design note: this page is intentionally neutral. The final dropzone, iconography, spacing and color system will be replaced from the design sheet.</div>
    </>
  );
}
