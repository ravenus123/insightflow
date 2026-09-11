import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "InsightFlow", template: "%s · InsightFlow" },
  description: "Premium business analytics and data automation for sales teams.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
