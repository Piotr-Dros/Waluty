'use client';

import dynamic from 'next/dynamic';
import LoadingSkeleton from './LoadingSkeleton';
import { PlotParams } from 'react-plotly.js';

const Plot = dynamic(() => import('react-plotly.js'), {
  ssr: false,
  loading: () => <LoadingSkeleton />,
});

export default function CustomPlot({
  data,
  layout,
  config,
  ...rest
}: PlotParams) {
  console.log(layout);
  return (
    <div className="my-4">
      <Plot
        className={`w-full rounded-md overflow-hidden ${rest.className}`}
        data={data}
        layout={{
          ...layout,
          title: '',
          xaxis: {
            title: '',
          },
          yaxis: {
            title: '',
          },
          legend: {
            orientation: 'h',
          },
        }}
        config={{
          modeBarButtonsToRemove: ['resetScale2d'],
          displaylogo: false,
          responsive: true,
          ...config,
        }}
        {...rest}
      />
    </div>
  );
}
