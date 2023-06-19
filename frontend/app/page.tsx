'use client';

import homepage from '@/styles/homepage.module.css';
import Link from 'next/link';
import { useCallback } from 'react';
export default function Home() {
  const mesaureGalleryRef = useCallback((gallery: HTMLDivElement) => {
    if (!gallery) return;
    const galleryMove = (e: MouseEvent) => {
      const mouseX = e.clientX;
      const mouseY = e.clientY;
      const xDecimal = mouseX / window.innerWidth;
      const yDecimal = mouseY / window.innerHeight;

      const maxX = gallery.offsetWidth - window.innerWidth;
      const maxY = gallery.offsetHeight - window.innerHeight;

      const panX = maxX * xDecimal * -1;
      const panY = maxY * yDecimal * -1;

      gallery.animate(
        {
          transform: `translate(${panX}px, ${panY}px)`,
        },
        {
          duration: 3000,
          fill: 'forwards',
          easing: 'ease',
        }
      );
      gallery.style.transform = `translate(${panX}px, ${panY}px)`;
    };

    window.addEventListener('mousemove', galleryMove);
  }, []);

  return (
    <main className="overflow-hidden">
      <div className={homepage.gallery} ref={mesaureGalleryRef}>
        <div className={homepage.tile}>
          <Link href="/graphs"></Link>
        </div>
        <div className={homepage.tile}>
          <Link href=""></Link>
        </div>
        <div className={homepage.tile}>
          <Link href=""></Link>
        </div>
        <div className={homepage.tile}>
          <Link href=""></Link>
        </div>
        <div className={homepage.tile}>
          <Link href=""></Link>
        </div>
      </div>
    </main>
  );
}
