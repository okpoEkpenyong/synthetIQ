import AccountList from '@components/Home/TopSales/AccountList'
import { useUserPreferences } from '@context/UserPreferences'
import { LoggerInstance } from '@oceanprotocol/lib'
import {
  getPublishers,
  getTopAssetsPublishers,
  UserSales
} from '@utils/aquarius'
import { ReactElement, useEffect, useState } from 'react'
import styles from './index.module.css'

export default function TopSales({
  title,
  action
}: {
  title: ReactElement | string
  action?: ReactElement
}): ReactElement {
  const { chainIds } = useUserPreferences()
  const [result, setResult] = useState<UserSales[]>([])
  const [loading, setLoading] = useState<boolean>()

  const [currentTime, setCurrentTime] = useState(0)

  useEffect(() => {
    async function init() {
      setLoading(true)
      if (chainIds.length === 0) {
        const result: UserSales[] = []
        setResult(result)
        setLoading(false)
      } else {
        try {
          const publishers = await getTopAssetsPublishers(chainIds)
          setResult(publishers)
          setLoading(false)
        } catch (error) {
          LoggerInstance.error(error.message)
          setLoading(false)
        }
      }
    }
    init()
  }, [chainIds])

  useEffect(() => {
    async function retrievePublishedDDOs() {
      try {
        const publisherrs = await getPublishers(chainIds, null)
        console.log({ publisherrs, chainIds })

        // await axios.post(flaskApiEndpoint, { data: publisherrs })
      } catch (error) {
        LoggerInstance.log('Error fetching data:', error)
      }
    }
    retrievePublishedDDOs()
  }, [chainIds])

  return (
    <section className={styles.section}>
      <h3>{title}</h3>
      {/* <p>The current time is {currentTime}.</p> */}
      <AccountList accounts={result} isLoading={loading} />
      {action && action}
    </section>
  )
}
