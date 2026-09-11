export function Logo({ compact = false }: { compact?: boolean }) {
  return (
    <div className="brand-lockup" aria-label="InsightFlow">
      <div className="brand-mark" aria-hidden="true">
        <span className="brand-mark-core" />
        <span className="brand-mark-orbit brand-mark-orbit-a" />
        <span className="brand-mark-orbit brand-mark-orbit-b" />
      </div>
      {!compact && <span className="brand-name">insight<span>flow</span></span>}
    </div>
  );
}
