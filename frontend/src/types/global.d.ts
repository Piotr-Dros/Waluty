import { Data, Layout } from 'plotly.js';

export {};

declare global {
  interface GraphJson {
    data: Data[];
    layout: Layout;
  }
}
