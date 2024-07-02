import React from 'react'
import { useSelector } from "react-redux"



function DeskU13() {

    const { thirteenthBooler } = useSelector(state => state.thirteenthBooler)
    console.log(useSelector(state => state.thirteenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: thirteenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{thirteenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">13</h5>
      </div>
    </div>
  </div>
  )
}

export default DeskU13
