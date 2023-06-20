import './globals.css';
import { Poppins } from 'next/font/google';
import Navigation from './Navigation';

const poppins = Poppins({ subsets: ['latin'], weight: '400' });

export const metadata = {
  title: 'Currency data visualisation',
  description: 'Visualisation project',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body
        className={`${poppins.className} min-h-screen grid grid-cols-main grid-rows-1`}
      >
        <Navigation />
        <div className="py-4 px-10 bg-gray-200 grow-[2]">{children}</div>
      </body>
    </html>
  );
}
