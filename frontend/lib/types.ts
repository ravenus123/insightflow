export type ColumnRole = "date" | "revenue" | "product" | "order_id" | "ignore";

export interface DatasetUploadResponse {
  dataset_id: string;
  filename: string;
  rows: number;
  columns: string[];
  preview: Record<string, unknown>[];
  detected_mapping: Partial<Record<Exclude<ColumnRole, "ignore">, string>>;
}

export interface AnalyticsResponse {
  metrics: {
    total_revenue: number;
    orders: number;
    average_order_value: number;
  };
  revenue_over_time: Array<{ date: string; revenue: number }>;
  top_products: Array<{ product: string; revenue: number; orders: number }>;
}
