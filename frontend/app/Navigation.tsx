import Image from 'next/image';
import NavItem, { NavItemProps } from './NavItem';

const navItems: NavItemProps[] = [
  {
    label: 'Wstęp',
    url: '/',
  },
  {
    label: 'Trendy Walut',
    url: '/trends',
  },
  {
    label: 'Analiza Polityczna - Świat',
    url: '/world',
  },
  {
    label: 'Analiza Polityczna - Polska',
    url: '/poland',
  },
  {
    label: 'Inflacja',
    url: '/inflation',
  },
  {
    label: 'Siła Nabywcza Pieniądza',
    url: '/money_power',
  },
];

export default function Navigation() {
  return (
    <nav className="px-8 py-4 text-white flex flex-col gap-20 shadow-inner">
      <div>
        <Image
          src={'/logo.png'}
          className="filter invert"
          alt="logo"
          width={300}
          height={100}
        />
      </div>
      <div>
        <ul className="list-none flex flex-col gap-2">
          {navItems.map((item) => (
            <NavItem key={item.label} {...item} />
          ))}
        </ul>
      </div>
    </nav>
  );
}
