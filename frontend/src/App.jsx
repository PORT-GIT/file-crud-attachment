import { useState } from 'react'
import './App.css'
import Sidebar from './Components/Sidebar'
import Titlelogo from './Components/Titlelogo'

function App() {
  

  return (
    <div className='flex'>
      <Sidebar />
      <Titlelogo />
    </div>
  )
}

export default App
