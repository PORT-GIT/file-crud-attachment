{/* has not been included in the routing at 
    app.jsx because it will be embedded in titlelogo.jsx*/}
import React from 'react'
import { FaBars, FaBell, FaUserCircle } from "react-icons/fa"
import { FaSearch } from "react-icons/fa"
import { IoMdArrowDropdown } from "react-icons/io";

const Navbar = () => {
  return (
    <nav className='bg-blue-500 flex justify-between px-4 py-3 ml-64'>

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

            <div className='text-white' ><FaBell className='w-6 h-6' /></div>

            <div className='relative'>
                <button className='text-white group'>
                    <FaUserCircle className='w-6 h-6 mt-2'/>
                    {/* to create a dropdown menu */}
                    <div className='bg-white z-10 hidden absolute rounded-lg shadow w-32 group-focus:block top-full right-0'>
                        <ul className='py-2 text-sm text-gray-950'>
                        <li>
                            <a href="#">Profile</a>
                        </li>

                        <li>
                            <a href="#">Settings</a>
                        </li>

                        <li>
                            <a href="#">Logout</a>
                        </li>
                    </ul>
                    </div>
                </button>
            </div>

        </div>

       
    
    </nav>
  )
}

export default Navbar