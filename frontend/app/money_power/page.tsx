import CustomPlot from '@/components/CustomPlot';
import { getGraph } from '@/utils/api';

export default async function InlationPage() {
  const data = await getGraph(6);

  return (
    <main className="py-4 px-10">
      <h1 className="text-center">Siła Nabywcza Pieniądza</h1>
      <CustomPlot
        data={data.data}
        layout={{ ...data.layout }}
        config={data.config}
      />
    </main>
  );
}
