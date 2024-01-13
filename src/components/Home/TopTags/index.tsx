import { useUserPreferences } from '@context/UserPreferences'
import { useCancelToken } from '@hooks/useCancelToken'
import { LoggerInstance } from '@oceanprotocol/lib'
import Loader from '@shared/atoms/Loader'
import Tags from '@shared/atoms/Tags'
import { ReactElement, useEffect, useState } from 'react'
import { getTopTags } from './_utils'
import styles from './index.module.css'

export default function TopTags({
  title,
  action
}: {
  title: ReactElement | string
  action?: ReactElement
}): ReactElement {
  const { chainIds } = useUserPreferences()
  const [result, setResult] = useState<string[]>([])
  const [loading, setLoading] = useState<boolean>()
  const newCancelToken = useCancelToken()

  useEffect(() => {
    async function init() {
      setLoading(true)
      if (chainIds.length === 0) {
        const result: string[] = []
        setResult(result)
        setLoading(false)
      } else {
        try {
          const tags = await getTopTags(chainIds, newCancelToken())
          setResult(tags)
          setLoading(false)
        } catch (error) {
          LoggerInstance.error(error.message)
          setLoading(false)
        }
      }
    }

    init()
  }, [chainIds])

  console.log('Top Tags:', result)
  return (
    <section className={styles.section}>
      <h3>{title}</h3>
      {loading ? <Loader /> : <Tags items={result} />}

      {action && action}
    </section>
  )
}
