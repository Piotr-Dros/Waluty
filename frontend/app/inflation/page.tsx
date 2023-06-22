import CustomDisclosure, {
  CustomDisclosureProps,
} from '@/components/CustomDisclosure';
import CustomPlot from '@/components/CustomPlot';
import CustomSwiper from '@/components/CustomSwiper';
import { getMultipleGraphs } from '@/utils/api';
import { config } from 'process';

const globalInfo: CustomDisclosureProps[] = [
  {
    label: '2004-2007',
    content: (
      <>
        Rozszerzenie Unii Europejskiej o nowe kraje, w tym Polskę, co wpłynęło
        na zmiany gospodarcze i handlowe w regionie.
      </>
    ),
  },
  {
    label: '2008-2009 (kryzys finansowy)',
    content: (
      <>
        Wrzesień 2008: Bank Lehman Brothers ogłosił bankructwo, co wywołuje
        globalny kryzys finansowy.
        <br />
        Skutkiem kryzysu finansowego jest spowolnienie gospodarcze na całym
        świecie, co ma wpływ na inflację w różnych krajach.
      </>
    ),
  },
  {
    label: '2010-2012 (kryzys zadłużeniowy w strefie euro)',
    content: (
      <>
        2010: Kryzys zadłużeniowy w strefie euro osiąga szczyt, szczególnie
        dotykając kraje takie jak Grecja, Hiszpania i Włochy.
        <br />
        Kryzys w strefie euro powoduje niepewność na rynkach finansowych, co
        może wpływać na wycenę walut i inflację.
      </>
    ),
  },
  {
    label: '2014-2016',
    content: (
      <>
        2014: Spadek cen ropy naftowej na światowych rynkach, co prowadzi do
        deflacji i obniżenia inflacji w wielu krajach, w tym w Polsce i Wielkiej
        Brytanii.
        <br />
        2015: Rezerwa Federalna (Fed) podnosi stopy procentowe w Stanach
        Zjednoczonych, co może wpływać na wartość dolara amerykańskiego.
      </>
    ),
  },
  {
    label: '2016-2018',
    content: (
      <>
        2016: Brexit - referendalne głosowanie w Wielkiej Brytanii, w wyniku
        którego kraj zdecydował o opuszczeniu Unii Europejskiej.
        <br />
        2016-2018: Negocjacje dotyczące Brexitu i niepewność co do przyszłych
        relacji handlowych między Wielką Brytanią a UE, co może wpływać na
        wartość funta brytyjskiego.
      </>
    ),
  },
  {
    label: '2019-2020 (pandemia COVID-19)',
    content: (
      <>
        2020: Globalna pandemia COVID-19 wpływa na gospodarki na całym świecie,
        prowadząc do recesji i wprowadzenia różnych środków zaradczych, takich
        jak lockdowny i pomoc finansowa.
        <br />
        Środki zaradcze podjęte w celu przeciwdziałania skutkom pandemii mogą
        wpływać na inflację, zwłaszcza w przypadku programów druku pieniędzy i
        łagodzenia polityki monetarnej.
      </>
    ),
  },
  {
    label: '2021-2023',
    content: (
      <>
        2021: Ożywienie gospodarcze po pandemii COVID-19, które może prowadzić
        do wzrostu popytu i wzrostu infl
      </>
    ),
  },
];

const russiaInfo: CustomDisclosureProps[] = [
  {
    label: '2004-2008',
    content: (
      <>
        Wzrost cen ropy naftowej na światowych rynkach, ponieważ Rosja jest
        jednym z największych producentów i eksporterów ropy naftowej na
        świecie. Wzrost cen ropy przyczyniał się do wzrostu dochodów z eksportu
        i wpływów do budżetu państwa.
      </>
    ),
  },
  {
    label: '2008-2009 (kryzys finansowy)',
    content: (
      <>
        Globalny kryzys finansowy, który miał negatywny wpływ na gospodarkę
        rosyjską, prowadząc do spowolnienia wzrostu gospodarczego i spadku
        popytu na rosyjskie towary eksportowe, takie jak ropa naftowa.
      </>
    ),
  },
  {
    label: '2014-2015 (kryzys walutowy)',
    content: (
      <>
        Upadek cen ropy naftowej na światowych rynkach, co spowodowało spadek
        dochodów z eksportu ropy i obniżenie wartości rosyjskiego rubla.
        Spadający kurs walutowy przyczynił się do wzrostu inflacji w Rosji.
      </>
    ),
  },
  {
    label: '2014-2017 (sankcje międzynarodowe)',
    content: (
      <>
        W 2014 roku Rosja została objęta sankcjami międzynarodowymi w związku z
        aneksją Krymu i zaangażowaniem w konflikt na wschodniej Ukrainie.
        Sankcje ograniczyły dostęp do zagranicznych rynków finansowych i
        technologii dla rosyjskich firm, co wpłynęło na gospodarkę i inflację.
      </>
    ),
  },
  {
    label: '2018-2019',
    content: (
      <>
        Wzrost cen żywności i podwyżki podatków (m.in. podatek VAT), które
        przyczyniły się do wzrostu inflacji w Rosji.
      </>
    ),
  },
  {
    label: '2020-2021 (pandemia COVID-19)',
    content: (
      <>
        Globalna pandemia COVID-19 spowodowała spowolnienie gospodarcze i
        wprowadzenie środków ograniczających działalność gospodarczą.
        Ograniczenia te wpłynęły na inflację poprzez zmniejszenie popytu i
        zakłócenie łańcuchów dostaw.
      </>
    ),
  },
  {
    label: '2022-2023',
    content: (
      <>
        Wzrost cen surowców, w tym ropy naftowej i gazu, co ma znaczący wpływ na
        rosyjską gospodarkę, ponieważ kraj jest jednym z największych
        producentów i eksporterów tych surowców. Wzrost cen surowców może
        przyczynić się do wzrostu inflacji w Rosji.
      </>
    ),
  },
];

export default async function InlationPage() {
  const datas = await getMultipleGraphs([3, 4, 5]);

  return (
    <main className="py-4 px-10">
      <h1 className="text-center">Inflacja</h1>
      <CustomSwiper>
        {datas.map((data) => (
          <CustomPlot
            key={data.data[0].name}
            data={data.data}
            layout={{ ...data.layout }}
            config={data.config}
          />
        ))}
      </CustomSwiper>
      <div className="p-4 rounded-md flex flex-col gap-2">
        {globalInfo.map((disclosureInfo) => (
          <CustomDisclosure key={disclosureInfo.label} {...disclosureInfo} />
        ))}
      </div>

      <div className="w-full h-1 my-10 bg-purple-300 rounded-lg shadow-md"></div>
      <h2>Rosja:</h2>
      <div className="p-4 rounded-md flex flex-col gap-2">
        {russiaInfo.map((disclosureInfo) => (
          <CustomDisclosure key={disclosureInfo.label} {...disclosureInfo} />
        ))}
      </div>
    </main>
  );
}
