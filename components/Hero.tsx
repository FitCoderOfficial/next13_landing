'use client'

import Image from "next/image"
import CustomButton from "./CustomButton"

const Hero = () => {
    const handlScroll = () => { 
    
    }


    return (
        <div className="hero">
            <div className="flex-1 pt-36 padding-x">
                <h1 className="hero__title">하루 세끼</h1>


                <p className="hero__subtitle">
                    하루에 먹은 칼로리를 계산하고 측정해보세요
                </p>

                <CustomButton 
                    title="찾아보기"
                    containerStyles="bg-primary-blue text-white mt-10 rounded-full"
                    handleClick={handlScroll}  

                    />
            </div>
        </div>
    )
}

export default Hero