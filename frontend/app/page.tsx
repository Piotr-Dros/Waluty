'use client';

import styles from '@/styles/home.module.css';
import CustomDialog from '@/components/CustomDialog';

export default function Home() {
  return (
    <main className="overflow-hidden py-4 px-10 isolate">
      <h1 className="text-center">Projekt z wizualizacji 2023/2024</h1>
      <article>
        <h2>Słowo wstępu</h2>
        Celem naszego projektu jest zrozumienie, jak pewne czynniki ekonomiczne,
        polityczne i geopolityczne mogą wpływać na wartość walut na rynkach
        międzynarodowych. Nasza praca koncentruje się na trzech głównych
        czynnikach:
        <b> inflacji</b>,<b> analizie politycznej i geopolitycznej</b> oraz
        <b> sile nabywczej pieniądza</b>.
      </article>
      <article>
        <h2>Wykorzystane technologie:</h2>
        <div className="gap-3 bg-white p-4 rounded-md grid grid-cols-2">
          <CustomDialog
            className="row-span-2"
            backgroundImage="/bsBG.png"
            title="Beautiful Soup"
          >
            Is a tool to scrap a page
          </CustomDialog>
          <CustomDialog
            title={
              <div className="grid place-items-center">
                <div
                  style={{
                    backgroundImage: 'url("/plotlyLogo.png")',
                    backgroundSize: 'cover',
                    backgroundPosition: 'center',
                  }}
                  className="min-h-[100px] w-[400px]"
                ></div>
              </div>
            }
            backgroundImage="/plotlyBG.png"
          >
            Plotly jest potężnym narzędziem do tworzenia interaktywnych wykresów
            w różnych środowiskach. Dzięki jego elastycznym funkcjom i
            intuicyjnemu interfejsowi możesz tworzyć wizualizacje danych, które
            pomogą zrozumieć i przedstawić informacje w atrakcyjny i
            interaktywny sposób.
            <div></div>
          </CustomDialog>
          <CustomDialog className="" backgroundImage="/nextBG.png" />
        </div>
      </article>
    </main>
  );
}
