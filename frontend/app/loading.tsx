import LoadingSkeleton from '@/components/LoadingSkeleton';

export default function loading() {
  return (
    <div className="w-full h-full grid place-items-center">
      <LoadingSkeleton />
    </div>
  );
}
