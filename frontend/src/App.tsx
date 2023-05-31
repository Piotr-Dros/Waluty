import './global.css';

import Graph from './components/Graph';
import { getSampleGraph } from './utils/api';

export default function App() {
  return (
    <div className="grid place-items-center min-h-screen">
      <Graph getGraphJson={getSampleGraph} />
    </div>
  );
}
