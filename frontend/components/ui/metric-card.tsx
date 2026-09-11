import { ArrowDownRight, ArrowUpRight } from "lucide-react";
import { GlassCard } from "./glass-card";

export function MetricCard({ label, value, delta, helper, icon }: { label: string; value: string; delta?: number; helper?: string; icon?: React.ReactNode }) {
  const positive = (delta ?? 0) >= 0;
  return (
    <GlassCard className="metric-card" interactive>
      <div className="metric-top"><span className="metric-label">{label}</span>{icon && <span className="metric-icon">{icon}</span>}</div>
      <div className="metric-value">{value}</div>
      <div className="metric-foot">
        {typeof delta === "number" && <span className={`trend ${positive ? "positive" : "negative"}`}>{positive ? <ArrowUpRight size={13}/> : <ArrowDownRight size={13}/>} {Math.abs(delta).toFixed(1)}%</span>}
        {helper && <span>{helper}</span>}
      </div>
      <div className="metric-shine" />
    </GlassCard>
  );
}
