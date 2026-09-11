import { ReactNode } from "react";

export function GlassCard({ children, className = "", interactive = false }: { children: ReactNode; className?: string; interactive?: boolean }) {
  return <section className={`glass-card ${interactive ? "glass-interactive" : ""} ${className}`.trim()}>{children}</section>;
}
