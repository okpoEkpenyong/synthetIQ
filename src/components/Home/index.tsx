import { ReactElement, useEffect, useState } from 'react'
import DatasetList from '../Home/Recommendations/DatasetList'
import styles from './index.module.css'

export default function HomePage(): ReactElement {
  const [recommendedData, setRecommendedData] = useState<PagedAssets>()

  useEffect(() => {
    async function getMetricsData() {
      try {
        const apiUrl = 'http://127.0.0.1:5100/api/recommendations'
        await fetch(apiUrl, { mode: 'cors' })
          .then((res) => res.json())
          .then((data) => {
            console.log({ data })
            setRecommendedData(data)
          })
      } catch (error) {}
    }

    getMetricsData()
  }, [])

  return (
    <>
      <section className={styles.section}>
        <div>
          <h1>Recommended Climate Data</h1>
          <DatasetList datasets={recommendedData} />
        </div>
      </section>
    </>
  )
}
