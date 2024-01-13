import { useMarketMetadata } from '@context/MarketMetadata'
import loadable from '@loadable/component'
import Logo from '@shared/atoms/Logo'
import Link from 'next/link'
import { useRouter } from 'next/router'
import { ReactElement } from 'react'
import styles from './Menu.module.css'
import SearchBar from './SearchBar'
import UserPreferences from './UserPreferences'
import Networks from './UserPreferences/Networks'
const Wallet = loadable(() => import('./Wallet'))

declare type MenuItem = {
  name: string
  link: string
}

function MenuLink({ item }: { item: MenuItem }) {
  const router = useRouter()

  const classes =
    router?.pathname === item.link
      ? `${styles.link} ${styles.active}`
      : styles.link

  return (
    <Link key={item.name} href={item.link} className={classes}>
      {item.name}
    </Link>
  )
}

export default function Menu(): ReactElement {
  const { siteContent } = useMarketMetadata()

  return (
    <nav className={styles.menu}>
      <Link href="/" className={styles.logo}>
        <Logo noWordmark />
        <h1 className={styles.title}>{siteContent?.siteTitle}</h1>
      </Link>

      {/* <ul className={styles.navigation}>
        {siteContent?.menu.map((item: MenuItem) => (
          <li key={item.name}>
            <MenuLink item={item} />
          </li>
        ))}
      </ul> */}

      <div className={styles.actions}>
        <SearchBar />
        <Networks />
        <Wallet />
        <UserPreferences />
      </div>
    </nav>
  )
}
