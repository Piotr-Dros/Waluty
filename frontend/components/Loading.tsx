import loadingGraphStyles from '@/styles/loadingGraph.module.css';

export default function loadingGraph() {
  return (
    <div className="w-full grid place-items-center mt-8">
      <span className={loadingGraphStyles.loader}>
        <span className={loadingGraphStyles['loader-inner']}></span>
      </span>
    </div>
  );
}
