'use client';

import { Disclosure } from '@headlessui/react';
import { FaAngleUp } from 'react-icons/fa';

export type CustomDisclosureProps = {
  label: string;
  content: string;
};

export default function CustomDisclosure({
  label,
  content,
}: CustomDisclosureProps) {
  return (
    <Disclosure>
      {({ open }) => (
        <>
          <Disclosure.Button className="flex w-full justify-between rounded-lg bg-purple-100 px-4 py-2 text-sm font-medium text-purple-900 hover:bg-purple-200 focus:outline-none focus-visible:ring focus-visible:ring-purple-500 focus-visible:ring-opacity-75">
            <span>{label}</span>
            <FaAngleUp
              className={`${
                open ? 'rotate-180 transform' : ''
              } h-5 w-5 text-purple-500`}
            />
          </Disclosure.Button>
          <Disclosure.Panel className="px-4 pt-1 pb-2 text-sm">
            {content}
          </Disclosure.Panel>
        </>
      )}
    </Disclosure>
  );
}
