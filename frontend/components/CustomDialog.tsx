'use client';

import { Dialog, Transition } from '@headlessui/react';
import { Fragment, ReactNode, useState } from 'react';

type CustomDialogProps = {
  label?: string;
  backgroundImage?: string;
  title?: ReactNode;
  children?: ReactNode;
  className?: string;
};

export default function CustomDialog({
  label,
  backgroundImage,
  title,
  children,
  className,
}: CustomDialogProps) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <button
        type="button"
        onClick={() => setIsOpen(true)}
        style={{
          backgroundImage: `url("${backgroundImage}")`,
          backgroundPosition: 'center',
          backgroundSize: 'cover',
        }}
        className={`${className} outline-none shadow-lg w-full rounded-md px-4 py-24 text-2xl font-medium text-white`}
      >
        {label}
      </button>

      <Transition appear show={isOpen} as={Fragment}>
        <Dialog
          as="div"
          className="relative z-10"
          onClose={() => setIsOpen(false)}
        >
          <Transition.Child
            as={Fragment}
            enter="ease-out duration-300"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="ease-in duration-200"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <div className="fixed inset-0 bg-black bg-opacity-25" />
          </Transition.Child>

          <div className="fixed inset-0 overflow-y-auto">
            <div className="flex min-h-full items-center justify-center p-4 text-center">
              <Transition.Child
                as={Fragment}
                enter="ease-out duration-300"
                enterFrom="opacity-0 scale-95"
                enterTo="opacity-100 scale-100"
                leave="ease-in duration-200"
                leaveFrom="opacity-100 scale-100"
                leaveTo="opacity-0 scale-95"
              >
                <Dialog.Panel className="min-w-[70vw] transform overflow-hidden rounded-md bg-white p-6 shadow-xl transition-all">
                  <Dialog.Title as="h3" className="text-2xl font-bold">
                    {title}
                  </Dialog.Title>
                  {children}
                </Dialog.Panel>
              </Transition.Child>
            </div>
          </div>
        </Dialog>
      </Transition>
    </>
  );
}
