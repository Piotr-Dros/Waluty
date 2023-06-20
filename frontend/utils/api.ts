import { Data, PlotlyDataLayoutConfig } from 'plotly.js';

const apiUrl = 'http://127.0.0.1:5000';

export async function getGraph(id: number): Promise<Data[]> {
  const res = await fetch(`${apiUrl}/api/graphs/${id}`);
  const data = (await res.json()) as PlotlyDataLayoutConfig;

  return data.data;
}
