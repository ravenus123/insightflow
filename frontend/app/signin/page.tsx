"use client";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { ArrowRight, LockKeyhole, Mail } from "lucide-react";
import { AmbientBackground } from "@/components/ambient-background";
import { Logo } from "@/components/logo";

export default function SignInPage(){ const router=useRouter(); return <div className="auth-shell"><AmbientBackground/><div className="auth-card reveal"><Link href="/"><Logo/></Link><div className="auth-copy"><div className="eyebrow"><span/>Welcome back</div><h1>Sign in to InsightFlow</h1><p>Use the demo access to explore the complete workspace.</p></div><form onSubmit={(e)=>{e.preventDefault();router.push('/overview')}}><label>Email<div className="field"><Mail size={17}/><input type="email" defaultValue="demo@insightflow.app" required/></div></label><label>Password<div className="field"><LockKeyhole size={17}/><input type="password" defaultValue="insightflow" required/></div></label><button className="button primary large full" type="submit">Continue <ArrowRight size={17}/></button></form><p className="auth-note">Portfolio demo — credentials are pre-filled. <Link href="/signup">Create account</Link></p></div></div> }
