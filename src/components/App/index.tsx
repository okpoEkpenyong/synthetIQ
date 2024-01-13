import Header from '@components/Header'
import { useMarketMetadata } from '@context/MarketMetadata'
import { useAccountPurgatory } from '@hooks/useAccountPurgatory'
import AnnouncementBanner from '@shared/AnnouncementBanner'
import Alert from '@shared/atoms/Alert'
import { ReactElement } from 'react'
import { ToastContainer } from 'react-toastify'
import { useAccount } from 'wagmi'
import contentPurgatory from '../../../content/purgatory.json'
import PrivacyPreferenceCenter from '../Privacy/PrivacyPreferenceCenter'
import styles from './index.module.css'

export default function App({
  children
}: {
  children: ReactElement
}): ReactElement {
  const { siteContent, appConfig } = useMarketMetadata()
  const { address } = useAccount()
  const { isInPurgatory, purgatoryData } = useAccountPurgatory(address)

  return (
    <div className={styles.app}>
      {siteContent?.announcement !== '' && (
        <AnnouncementBanner text={siteContent?.announcement} />
      )}
      <Header />

      {isInPurgatory && (
        <Alert
          title={contentPurgatory.account.title}
          badge={`Reason: ${purgatoryData?.reason}`}
          text={contentPurgatory.account.description}
          state="error"
        />
      )}
      <main className={styles.main}>{children}</main>
      {/* <Footer /> */}

      {appConfig?.privacyPreferenceCenter === 'true' && (
        <PrivacyPreferenceCenter style="small" />
      )}

      <ToastContainer position="bottom-right" newestOnTop />
    </div>
  )
}
