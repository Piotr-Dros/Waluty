import loadingGraphStyles from '@/styles/loadingGraph.module.css';

export default function LoadingSkeleton() {
  return (
    <div className="w-full grid place-items-center my-28">
      <span className={loadingGraphStyles.loader}>
        <span className={loadingGraphStyles['loader-inner']}></span>
      </span>
    </div>
  );
}
