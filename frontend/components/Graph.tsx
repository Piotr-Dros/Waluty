import { PlotlyDataLayoutConfig } from 'plotly.js';
import { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';

type Props = {
  getGraphJson: (...args: any[]) => Promise<PlotlyDataLayoutConfig | null>;
};

function Graph({ getGraphJson }: Props) {
  const [graphJson, setGraphJson] = useState<PlotlyDataLayoutConfig | null>(
    null
  );

  useEffect(() => {
    getGraphJson().then((graphJson) => setGraphJson(graphJson));
  }, [graphJson]);

  if (!graphJson || !graphJson.layout) return <></>;

  return (
    <div className="p-6 shadow-2xl rounded-lg bg-purple-500">
      <Plot
        data={graphJson.data}
        layout={graphJson.layout}
        config={graphJson.config}
      />
    </div>
  );
}

export default Graph;
