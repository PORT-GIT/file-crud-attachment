import { useState } from 'react'


function Navbar() {
  
  return (
    <div className='side-nav flex-1 bg-blue-600'>

        <div className='title'>
            Registry File Tracker
        </div>

        <div className='nav-tabs'>
            <ul>
                <li> <a href="#">Dashboard</a></li>
                <li> <a href="#">Filelogs</a></li>
                <li> <a href="#">Filemovement</a></li>
            </ul> 
        </div>

    </div>
  )
}

export default Navbar
