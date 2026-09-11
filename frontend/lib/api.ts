import type { AnalyticsResponse, QualityResponse, UploadResponse } from "./types";

const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000/api/v1";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, init);
  if (!response.ok) {
    let detail = "Something went wrong.";
    try { const body = await response.json(); detail = body.detail ?? detail; } catch {}
    throw new Error(detail);
  }
  return response.json() as Promise<T>;
}

export async function uploadDataset(file: File): Promise<UploadResponse> {
  const form = new FormData(); form.append("file", file);
  return request<UploadResponse>("/datasets/upload", { method: "POST", body: form });
}
export async function getQuality(datasetId: string, mapping: Record<string,string>): Promise<QualityResponse> {
  return request<QualityResponse>(`/datasets/${datasetId}/quality`, { method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify({mapping}) });
}
export async function analyzeDataset(datasetId: string, mapping: Record<string,string>): Promise<AnalyticsResponse> {
  return request<AnalyticsResponse>(`/datasets/${datasetId}/analyze`, { method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify({mapping}) });
}
export { API_BASE };
