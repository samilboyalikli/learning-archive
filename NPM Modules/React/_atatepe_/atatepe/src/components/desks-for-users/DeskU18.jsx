import React from 'react'
import { useSelector } from "react-redux"



function DeskU18() {

  const { eighteenthBooler } = useSelector(state => state.eighteenthBooler)
  console.log(useSelector(state => state.eighteenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: eighteenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{eighteenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">18</h5>
      </div>
    </div>
  </div>
  )
}

export default DeskU18
