import { CustomFilter, Hero, SearchBar, StuffCard } from '@/components'
import { fetchData } from '@/utils'
import Image from 'next/image'


export default async function Home() {

  const allStuffs = await fetchData()

  const isDataEmpy = !Array.isArray(allStuffs) || allStuffs.length < 1 || !allStuffs;


  return (
    <main className="overflow-hidden">
      <Hero />
      <div className='mt-12 padding-x padding-y max-width' id='discover'>
        <div className='home__text-container'>
          <h1 className='text-4xl font-extrabold'>음식 카달로그</h1>
          <p>오늘 먹었던 음식들을 골라주세요</p>
        </div>

        <div className='home__filters'>
          <SearchBar />
          <div className='home__filter-container'>
            <CustomFilter title="fuel" />
            <CustomFilter title="year" />
          </div>
        </div>

        { !isDataEmpy ? (
          <section>
            <div className='home__cars-wrapper'>
              {allStuffs?.map((item) => (
                <StuffCard item={item} />
              ))}
            </div>
          </section>
        ) : (
          <div className='home__error-container'>
           <h2 className='text-black text-xl font-bold'>해당 항목이 없습니다</h2> 
           <p>{allStuffs?.message}</p>
          </div>
        )}

      </div>
    </main>
  )
}
