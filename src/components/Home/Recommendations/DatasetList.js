import AssetType from '@components/@shared/AssetType'
import NetworkName from '@components/@shared/NetworkName'
import Publisher from '@components/@shared/Publisher'
import Link from 'next/link'
import Dotdotdot from 'react-dotdotdot'
import StarRating from '../Recommendations/StarRating'
import styles from './index.module.css'

const DatasetList = ({ datasets }) => {
  // const { name, type, description } = datasets.ddo

  return (
    <div>
      {/* <h2>Recommended Datasets</h2> */}
      <ul>
        {datasets?.map((dataset, index) => {
          // Extract metadata from the deeply nested structure
          const metadata = dataset?.ddo?.metadata
          const did = dataset?.ddo?.id
          const type = metadata.type
          const datatokens = dataset?.ddo?.datatokens
          const accessType = dataset?.ddo?.services[0].type
          const chainId = dataset?.ddo?.chainId
          const nft = dataset?.ddo?.nft
          const stats = dataset?.ddo?.stats

          console.log({
            dataset,
            index,
            metadata,
            did,
            type,
            datatokens,
            accessType,
            chainId
          })

          return (
            <>
              <article
                key={index}
                className={`${styles.teaser} ${styles[metadata.type]}`}
              >
                <Link href={`/asset/${did}`} className={styles.link}>
                  <aside className={styles.detailLine}>
                    <AssetType
                      className={styles.typeLabel}
                      type={type}
                      accessType={accessType}
                    />
                    <span className={styles.typeLabel}>
                      {datatokens[0]?.symbol.substring(0, 9)}
                    </span>
                    <NetworkName
                      networkId={chainId}
                      className={styles.typeLabel}
                    />
                  </aside>
                  <header className={styles.header}>
                    <Dotdotdot tagName="h1" clamp={3} className={styles.title}>
                      {metadata.name.slice(0, 200)}
                    </Dotdotdot>
                    {<Publisher account={nft.owner} minimal />}
                  </header>
                  <footer>
                    {stats.orders && stats.orders > 0 ? (
                      <span className={styles.typeLabel}>
                        {stats.orders < 0 ? (
                          'N/A'
                        ) : (
                          <>
                            <strong>{stats.orders}</strong>{' '}
                            {stats.orders === 1 ? 'sale' : 'sales'}
                          </>
                        )}
                      </span>
                    ) : null}
                  </footer>
                  <div>
                    <div>
                      {'Completeness:'}:{dataset?.completeness}
                    </div>
                    <div>
                      {'Data Format Consistency:'}:
                      {dataset?.data_format_consistency}
                    </div>
                    <div>
                      {'Geo Coverage:'}:{dataset.geo_coverage.toFixed(2)}
                    </div>
                    <div>
                      {'Metadata Availability:'}:
                      {dataset.metadata_availability.toFixed(2)}
                    </div>
                    <div>
                      {'Temporaral Coverage:'}:
                      {dataset?.temporaral_coverage.toFixed(2)}
                    </div>
                    <StarRating
                      rating={dataset?.overall_quality * 5}
                      value={`${(100 * 5 * dataset.overall_quality).toFixed(
                        2
                      )} %`}
                      maxStars={5}
                      title={'Overall Quality'}
                    />
                  </div>
                </Link>
              </article>
            </>
          )
        })}
      </ul>
    </div>
  )
}

export default DatasetList
