import styles from '@/styles/BulletList.module.css';

import { Children } from 'react';

type Props = {
  children: React.ReactNode;
};

export default function CustomBulletList({ children }: Props) {
  return (
    <ul className={styles.container}>
      {Children.map(children, (child) => (
        <li className={styles.child}>{child}</li>
      ))}
    </ul>
  );
}
