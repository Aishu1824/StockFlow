import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export interface Product {
  id: number;
  name: string;
  description: string | null;
  price: string;
  sku: string;
}

export async function getProducts(): Promise<Product[]> {
  const response = await api.get("/products/");
  return response.data;
}