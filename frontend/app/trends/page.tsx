import CustomDisclosure, {
  CustomDisclosureProps,
} from '@/components/CustomDisclosure';
import CustomPlot from '@/components/CustomPlot';
import { getGraph } from '@/utils/api';

const disclosureInfo: CustomDisclosureProps[] = [
  {
    label: 'Kryzys finansowy 2008-2009',
    content:
      'Rozpoczęty w Stanach Zjednoczonych kryzys finansowy spowodował ogólnoświatową recesję. Spadek zaufania do systemu finansowego doprowadził do dużych fluktuacji na rynkach walutowych.',
  },
  {
    label: 'Brexit',
    content:
      'W 2016 roku mieszkańcy Wielkiej Brytanii opowiedzieli się za opuszczeniem Unii Europejskiej. Proces negocjacji i niepewność związana z przyszłością brytyjskiej gospodarki wpłynęły na kurs funta szterlinga.',
  },
  {
    label: 'Kryzys zadłużenia w strefie euro',
    content:
      'W latach 2010-2012 wiele krajów strefy euro znalazło się w trudnej sytuacji finansowej, co doprowadziło do spadku wartości euro i zwiększenia fluktuacji na rynku walutowym.',
  },
  {
    label: 'Polityka banku centralnego',
    content:
      'Decyzje podejmowane przez banki centralne, takie jak podniesienie lub obniżenie stóp procentowych, mogą wpływać na kursy walut. Na przykład, polityka luzowania ilościowego prowadzona przez Rezerwę Federalną w Stanach Zjednoczonych miała wpływ na wartość dolara amerykańskiego.',
  },
  {
    label: 'Kryzys finansowy w Grecji',
    content:
      'Kryzys zadłużenia w Grecji w latach 2009-2015 miał duży wpływ na stabilność euro i kurs euro względem innych walut. Obawy dotyczące trwałości strefy euro spowodowały wahania na rynku walutowym.',
  },
  {
    label: 'Konflikty geopolityczne',
    content:
      'Konflikty zbrojne i napięcia geopolityczne, takie jak wojna w Iraku, wojna domowa w Syrii czy napięcia na Półwyspie Koreańskim, mogą wpływać na kursy walut. W momencie wzrostu ryzyka geopolitycznego inwestorzy często szukają bezpiecznych przystani, co może wpłynąć na kursy walut takich jak japoński jen lub szwajcarski frank.',
  },
];

export default async function TrendsPage() {
  const data = await getGraph(1);

  return (
    <main className="py-4 px-10">
      <h1 className="text-center">Trendy Walut</h1>
      Poniżej przedstawiam kilka najważniejszych wydarzeń gospodarczych, które
      miały wpływ na kursy walut w ciągu ostatnich 20 lat:
      <CustomPlot
        className="w-full rounded-md overflow-hidden"
        data={data}
        layout={{}}
      />
      <div className="shadow-md p-4 bg-white rounded-md flex flex-col gap-2">
        {disclosureInfo.map((disclosureInfo) => (
          <CustomDisclosure key={disclosureInfo.label} {...disclosureInfo} />
        ))}
      </div>
    </main>
  );
}
