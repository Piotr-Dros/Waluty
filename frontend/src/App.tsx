import { useEffect, useState } from 'react';
import Graph from './components/Graph';
import { PlotlyDataLayoutConfig } from 'plotly.js';

export default function App() {
  const [graph, setGraph] = useState<PlotlyDataLayoutConfig | null>(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/graphs')
      .then((res) => res.json())
      .then((jsonGraph) => {
        setGraph(jsonGraph);
        console.log(jsonGraph);
      })
      .catch((error) => {
        console.error('Error fetching graph data:', error);
      });
  }, []);

  return (
    <div>
      <Graph graphJson={graph} />
    </div>
  );
}
