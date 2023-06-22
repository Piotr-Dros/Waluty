'use client';

import { Splide, SplideSlide } from '@splidejs/react-splide';
import '@splidejs/react-splide/css';
import { Children } from 'react';
import CustomDisclosure from './CustomDisclosure';

type Props = {
  children?: React.ReactNode;
};

export default function CustomSwiper({ children }: Props) {
  return (
    <Splide className="my-4" options={{}}>
      {Children.map(children, (child) => (
        <SplideSlide className="p-2">{child}</SplideSlide>
      ))}
    </Splide>
  );
}
