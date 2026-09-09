export function MetricCard({ label, value }: { label: string; value: string }) {
  return <div className="card metric"><div className="label">{label}</div><div className="value">{value}</div></div>;
}
