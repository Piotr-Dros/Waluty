import CustomDisclosure from '@/components/CustomDisclosure';
import CustomPlot from '@/components/CustomPlot';
import { getMultipleGraphs } from '@/utils/api';

export default async function InlationPage() {
  const datas = await getMultipleGraphs([24, 25]);
  return (
    <main className="py-4 px-10">
      <h1 className="text-center">Analiza Polityczna - Polska</h1>
      <div className="p-4 rounded-md flex flex-col gap-2">
        {datas.map((data) => (
          <CustomDisclosure
            key={data.data[0].name}
            // @ts-ignore
            label={data.layout?.title?.text}
            content={
              <>
                <CustomPlot
                  data={data.data}
                  layout={{ ...data.layout }}
                  config={data.config}
                />
              </>
            }
          />
        ))}
      </div>
    </main>
  );
}
