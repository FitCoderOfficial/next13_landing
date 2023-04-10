'use client'
import { useState } from "react"


import { SearchFood } from "./"

const SearchBar = () => {
    const [Food, setFood] = useState('')

    const handleSearch = () => { }
    return (
        <form className='searchbar' onSubmit={handleSearch}>
            <div className="searchbar__item">
                <SearchFood 
                    food={Food}
                    setFood={setFood}
                />
            </div>
        </form>
    )
}

export default SearchBar