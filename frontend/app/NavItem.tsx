'use client';

import { usePathname } from 'next/navigation';
import Link from 'next/link';
import classNames from 'classnames';
import { FaLongArrowAltRight } from 'react-icons/fa';

export type NavItemProps = {
  label: string;
  url: string;
};

export default function NavItem({ label, url }: NavItemProps) {
  const pathname = usePathname();

  const isActive = pathname === url;

  const classes = classNames('text-lg', {
    'text-purple-400': isActive,
  });

  return (
    <li className={classes}>
      <Link href={url} className="flex gap-1 items-center">
        {label}
        {isActive && <FaLongArrowAltRight />}
      </Link>
    </li>
  );
}
