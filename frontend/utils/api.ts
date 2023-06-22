import { PlotlyDataLayoutConfig } from 'plotly.js';

const apiUrl = 'http://127.0.0.1:5000';

export async function getGraph(id: number): Promise<PlotlyDataLayoutConfig> {
  const res = await fetch(`${apiUrl}/api/graphs/${id}`);
  const data = (await res.json()) as PlotlyDataLayoutConfig;
  return data;
}

export async function getMultipleGraphs(
  numbers: number[]
): Promise<PlotlyDataLayoutConfig[]> {
  const urls = numbers.map((number) => `${apiUrl}/api/graphs/${number}`);
  const fetchPromises = urls.map((url) => fetch(url).then((res) => res.json()));
  const data = (await Promise.all(fetchPromises)) as PlotlyDataLayoutConfig[];

  return data;
}
