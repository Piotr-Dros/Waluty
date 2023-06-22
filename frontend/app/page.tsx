'use client';

import CustomDialog from '@/components/CustomDialog';
import Image from 'next/image';

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
        <div className="gap-3 p-4 rounded-md grid grid-cols-2">
          <CustomDialog
            className="row-span-2 hover:scale-[1.02] transition duration-300"
            backgroundImage="/bsBG.png"
            title={
              <div className="grid place-items-center">
                <Image
                  src="/bsLogo.jpg"
                  alt="Beaufiul soup"
                  width={400}
                  height={100}
                />
              </div>
            }
          >
            Beautiful Soup to popularna biblioteka do analizy i przetwarzania
            danych HTML i XML w języku Python. Jest wykorzystywana głównie do
            ekstrakcji informacji ze stron internetowych, skrapowania danych i
            analizy struktury dokumentów. Oto kilka powodów, dla których warto
            rozważyć użycie Beautiful Soup w swoim projekcie:
          </CustomDialog>
          <CustomDialog
            className="hover:scale-[1.02] transition duration-300"
            title={
              <div className="grid place-items-center">
                <Image
                  src="/plotlyLogo.png"
                  alt="Plotly"
                  width={400}
                  height={100}
                />
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
          <CustomDialog
            className="hover:scale-[1.02] transition duration-300"
            title={
              <div className="grid place-items-center">
                <Image
                  src="/nextLogo.png"
                  alt="Next.js"
                  width={400}
                  height={100}
                />
              </div>
            }
            backgroundImage="/nextBG.png"
          >
            Next.js to popularny framework do budowania aplikacji webowych
            opartych na React.js. Oferuje wiele korzyści i rozwiązań, takich jak
            renderowanie po stronie serwera
          </CustomDialog>
        </div>
      </article>
    </main>
  );
}
