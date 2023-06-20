'use client';

import dynamic from 'next/dynamic';
import LoadingGraph from './Loading';
import { PlotParams } from 'react-plotly.js';

const Plot = dynamic(() => import('react-plotly.js'), {
  ssr: false,
  loading: () => <LoadingGraph />,
});

export default function CustomPlot({ data, layout, ...rest }: PlotParams) {
  return <Plot data={data} layout={layout} {...rest} />;
}
