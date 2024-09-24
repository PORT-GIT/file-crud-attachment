import React from 'react'
import { FaHome } from "react-icons/fa"
import { LuFileStack } from "react-icons/lu"
import { FaFileExport } from "react-icons/fa6"

const Sidebar = () => {
  return (
    <div className='w-64 bg-blue-500 fixed h-full px-2 py-2'>

        <div className='my-2 mb-4'>
            <h1 className='font-bold text-white text-xl'>Registry File Tracker</h1>

        </div>

        <hr/>
        
        <ul className='mt-3 font-bold text-white'>

            <li className='mb-2 rounded hover:shadow hover:bg-green-500 py-2'>
                {/* py puts padding for top and bottom */}
                <a href="#" className='px-3'>
                    {/* px puts padding to the right and left */}
                    <FaHome className='inline-block w-6 h-6 mr-2 -mt-2'></FaHome>
                    Dashboard
                </a>
            </li>

            
            <li className='mb-2 rounded hover:shadow hover:bg-green-500 py-2'>
                {/* py puts padding for top and bottom */} 
                <a href="#" className='px-3'>
                    {/* px puts padding to the right and left */}
                    <LuFileStack className='inline-block w-6 h-6 mr-2 -mt-2'></LuFileStack>
                    Filelogs
                </a>
            </li>

            
            <li className='mb-2 rounded hover:shadow hover:bg-green-500 py-2'>
                {/* py puts padding for top and bottom */}
                <a href="#" className='px-3'>
                    {/* px puts padding to the right and left */}
                    <FaFileExport className='inline-block w-6 h-6 mr-2 -mt-2'></ FaFileExport>
                    Filemovement
                </a>
            </li>
        </ul>

    </div>

    
  )
}

export default Sidebar