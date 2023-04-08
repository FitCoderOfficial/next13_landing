import { Footer, Navbar } from '@/components'
import './globals.css'


export const metadata = {
  title: '하루 세끼',
  description: '하루에 먹은 칼로리를 계산하고 측정해보세요',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ko">
      <body className='relative'>
        <Navbar />
        {children}
        <Footer />
      </body>
    </html>
  )
}
