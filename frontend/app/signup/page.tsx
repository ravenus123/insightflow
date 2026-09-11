"use client";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { ArrowRight, LockKeyhole, Mail, UserRound } from "lucide-react";
import { AmbientBackground } from "@/components/ambient-background";
import { Logo } from "@/components/logo";
export default function SignUpPage(){ const router=useRouter(); return <div className="auth-shell"><AmbientBackground/><div className="auth-card reveal"><Link href="/"><Logo/></Link><div className="auth-copy"><div className="eyebrow"><span/>New workspace</div><h1>Create your account</h1><p>Start with the included retail demo, then bring your own data.</p></div><form onSubmit={(e)=>{e.preventDefault();router.push('/overview')}}><label>Name<div className="field"><UserRound size={17}/><input defaultValue="Adam V." required/></div></label><label>Email<div className="field"><Mail size={17}/><input type="email" defaultValue="adam@example.com" required/></div></label><label>Password<div className="field"><LockKeyhole size={17}/><input type="password" defaultValue="insightflow" required/></div></label><button className="button primary large full" type="submit">Create workspace <ArrowRight size={17}/></button></form><p className="auth-note">Already have an account? <Link href="/signin">Sign in</Link></p></div></div> }
