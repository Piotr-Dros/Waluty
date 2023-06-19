import { Data, Layout } from 'plotly.js';
import { useState } from 'react';
import Plot from 'react-plotly.js';

type Props = {
  data: Data;
};

function Graph({ data }: Props) {
  const [graphData, setGraphData] = useState<Data[] | null>(null);

  const layout: Partial<Layout> = {
    title: 'Sample Graph',
  };

  if (!data) return <></>;

  return <div></div>;
}

export default Graph;
