"use client";

import { Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { MetricCard } from "@/components/ui/metric-card";
import { PageHeader } from "@/components/ui/page-header";
import { topProducts } from "@/lib/mock-data";

const chartData = [
  { date: "Jan 01", revenue: 12400 }, { date: "Jan 08", revenue: 18100 }, { date: "Jan 15", revenue: 15800 },
  { date: "Jan 22", revenue: 21900 }, { date: "Feb 01", revenue: 19800 }, { date: "Feb 08", revenue: 24700 },
  { date: "Feb 15", revenue: 23200 }, { date: "Mar 01", revenue: 28420 }
];

export default function DashboardPage() {
  return (
    <>
      <PageHeader title="Retail Sales" description="Jan 1 – Mar 31, 2026 · generated from semantic sales fields." />
      <div className="grid grid-3">
        <MetricCard label="Total revenue" value="€184,320" />
        <MetricCard label="Orders" value="2,481" />
        <MetricCard label="Average order value" value="€74.29" />
      </div>
      <div style={{ height: 16 }} />
      <section className="card card-pad">
        <div className="eyebrow">Revenue over time</div>
        <div style={{ height: 320, marginTop: 12 }}>
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={chartData}>
              <XAxis dataKey="date" tickLine={false} axisLine={false} />
              <YAxis tickLine={false} axisLine={false} />
              <Tooltip />
              <Line type="monotone" dataKey="revenue" stroke="currentColor" strokeWidth={2} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </section>
      <div style={{ height: 16 }} />
      <section className="card">
        <div className="card-pad"><div className="eyebrow">Top products</div></div>
        <div className="table-wrap"><table><thead><tr><th>Product</th><th>Revenue</th></tr></thead><tbody>{topProducts.map(([product, revenue]) => <tr key={product}><td>{product}</td><td>{revenue}</td></tr>)}</tbody></table></div>
      </section>
    </>
  );
}
