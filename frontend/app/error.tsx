'use client';

export default function ErrorPage({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <main className="grid place-content-center min-h-screen">
      <h2>Oops!</h2>
      <button
        onClick={() => reset()}
        className="p-2 rounded-md bg-purple-300 hover:scale-105 duration-150"
      >
        Try again
      </button>
    </main>
  );
}
