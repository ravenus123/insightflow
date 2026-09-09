import type { AnalyticsResponse, DatasetUploadResponse } from "./types";

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000/api/v1";

export async function uploadDataset(file: File): Promise<DatasetUploadResponse> {
  const body = new FormData();
  body.append("file", file);
  const response = await fetch(`${API_URL}/datasets/upload`, { method: "POST", body });
  if (!response.ok) throw new Error("Dataset upload failed");
  return response.json();
}

export async function analyzeDataset(datasetId: string, mapping: Record<string, string>): Promise<AnalyticsResponse> {
  const response = await fetch(`${API_URL}/datasets/${datasetId}/analyze`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mapping })
  });
  if (!response.ok) throw new Error("Dataset analysis failed");
  return response.json();
}
