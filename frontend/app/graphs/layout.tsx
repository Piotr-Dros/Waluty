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
    <div>
      <header className="grid place-items-center bg-gray-300 py-5 px-2">
        <h1>Kursy Walut na przestrzeni lat</h1>
      </header>
      {children}
    </div>
  );
}
