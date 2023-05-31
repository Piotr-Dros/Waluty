import { PlotlyDataLayoutConfig } from 'plotly.js';

export async function getSampleGraph(): Promise<PlotlyDataLayoutConfig | null> {
  try {
    const jsonGraph = (await fetch('http://127.0.0.1:5000/api/graphs').then(
      (res) => res.json()
    )) as PlotlyDataLayoutConfig;

    return jsonGraph;
  } catch (error) {
    console.error('Failed to fetch graph:', error);
    return null;
  }
}
