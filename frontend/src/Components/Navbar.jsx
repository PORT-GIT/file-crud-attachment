{/* has not been included in the routing at 
    app.jsx because it will be embedded in titlelogo.jsx*/}
import React from 'react'
import { FaBars } from "react-icons/fa"
import { FaSearch } from "react-icons/fa"

const Navbar = () => {
  return (
    <div className='bg-blue-500 flex justify-between px-4 py-3 ml-64'>

    <div className='left-side flex items-center text-xl'>
        <FaBars className='text-white me-4 cursor-pointer'></FaBars>
        <span className='text-white font-semibold'>Welcome, User</span>
    </div>

    <div className='right-side flex items-center gap-x-5'>
        <div className='relative md:w-65'>

            <span className='relative md:absolute inset-y-0 flex items-center pl-2'>
                <button className='p-1 focus:outline-none text-white md:text-black'>
                    <FaSearch />
                </button>
            </span>

            <input type="text" className='w-full px-4 py-1 pl-12 rounded shadow outline-none hidden md:block' />
        </div>
    </div>

    </div>
  )
}

export default Navbar