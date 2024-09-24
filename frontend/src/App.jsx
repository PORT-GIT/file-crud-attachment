import { useState } from 'react'
import './App.css'
import Sidebar from './Components/Sidebar'
import Titlelogo from './Components/Titlelogo'

function App() {
  // adding a state
  const [sidebarToggle, setSidebarToggle] = useState(false)
  return (
    <div className='flex'>
      <Sidebar sidebarToggle={sidebarToggle}/>
      <Titlelogo sidebarToggle={sidebarToggle}
        setSidebarToggle
       />
    </div>
  )
}

export default App
