'use client'

import React from 'react'
import Image from 'next/image'
import CustomButton from './CustomButton'
import { itemProps } from '@/types'
import { calculateCarRent } from '@/utils'
import { it } from 'node:test'

interface itemCardProps {
    item: itemProps
}

const StuffCard = ({ item }: itemCardProps) => {

    const { city_mpg, year, make, model, transmission, drive } = item

    const itemInfo = calculateCarRent(city_mpg, year,)

    return (
        <div className='car-card group'>
            <div className='car-card__content'>
                <h2 className='car-card__content-title'>
                    {make} {model}
                </h2>
            </div>

            <p className='flex mt-6 text-[32px] font-extrabold'>
                <span className='self-start text-[14px] font-semibold'>
                    $
                </span>
                {itemInfo}
                <span className='self-end text-[14px] font-medium'>
                    /day
                </span>
            </p>
            <div className='relative w-full h-40 my-3 object-contain'>
                <Image src="/hero.png" alt='item' fill priority className='object-contain' />
            </div>
        </div>
    )
}

export default StuffCard