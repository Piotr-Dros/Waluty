import CustomDisclosure from '@/components/CustomDisclosure';
import CustomPlot from '@/components/CustomPlot';
import { getMultipleGraphs } from '@/utils/api';

export default async () => {
  const datas = await getMultipleGraphs([
    7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
  ]);

  return (
    <main className="py-4 px-10">
      <h1 className="text-center">Analiza Polityczna - Świat</h1>
      <section>
        <h2>Wybuch wojny na ukrainie:</h2>
        <div className="p-4 rounded-md flex flex-col gap-2">
          {datas.slice(0, 6).map((data) => (
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
      </section>
      <section>
        <h2>Spadek cen ropy (2014-2015):</h2>
        <div className="p-4 rounded-md flex flex-col gap-2">
          {datas.slice(6, 11).map((data) => (
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
      </section>
      <section>
        <h2>Rozszerzenie Uni Europejskiej:</h2>
        <div className="p-4 rounded-md flex flex-col gap-2">
          {datas.slice(11).map((data) => (
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
      </section>
    </main>
  );
};
