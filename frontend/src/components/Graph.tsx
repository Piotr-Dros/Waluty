import { PlotlyDataLayoutConfig } from 'plotly.js';
import Plot from 'react-plotly.js';

type Props = {
  graphJson: PlotlyDataLayoutConfig | null;
};

function Graph({ graphJson }: Props) {
  if (!graphJson || !graphJson.layout) return <></>;

  return <Plot data={graphJson.data} layout={graphJson.layout} />;
}

export default Graph;
