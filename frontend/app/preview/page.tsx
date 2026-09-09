import Link from "next/link";
import { PageHeader } from "@/components/ui/page-header";
import { previewRows } from "@/lib/mock-data";

const mappings = [
  ["Date", "order_date", "High confidence"],
  ["Revenue", "total_price", "High confidence"],
  ["Product", "product_name", "High confidence"],
  ["Order ID", "order_id", "High confidence"]
];

export default function PreviewPage() {
  return (
    <>
      <PageHeader title="Retail Sales Q1" description="84,291 rows · 9 columns · review detected semantic fields before analysis." />
      <div className="grid grid-2">
        <section className="card card-pad">
          <div className="eyebrow">Detected fields</div>
          <div className="mapping-list" style={{ marginTop: 8 }}>
            {mappings.map(([role, column, confidence]) => (
              <div className="mapping-row" key={role}>
                <strong>{role}</strong>
                <select className="select" defaultValue={column}><option>{column}</option><option>Ignore</option></select>
                <span className="badge">{confidence}</span>
              </div>
            ))}
          </div>
        </section>
        <section className="card card-pad">
          <div className="eyebrow">Dataset metadata</div>
          <h2>retail_sales.csv</h2>
          <p style={{ color: "var(--muted)" }}>Temporary dataset · CSV · EUR</p>
          <div className="notice">Column mapping is a first-class product concept. Analytics uses semantic roles, never hard-coded source column names.</div>
        </section>
      </div>
      <div style={{ height: 16 }} />
      <section className="card">
        <div className="card-pad"><div className="eyebrow">Data preview</div></div>
        <div className="table-wrap">
          <table><thead><tr>{Object.keys(previewRows[0]).map((key) => <th key={key}>{key}</th>)}</tr></thead>
          <tbody>{previewRows.map((row, i) => <tr key={i}>{Object.values(row).map((value, j) => <td key={j}>{String(value)}</td>)}</tr>)}</tbody></table>
        </div>
      </section>
      <div className="actions"><Link className="button" href="/upload">Back</Link><Link className="button primary" href="/dashboard">Generate dashboard</Link></div>
    </>
  );
}
