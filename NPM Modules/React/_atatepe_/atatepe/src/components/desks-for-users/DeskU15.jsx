import React from 'react'
import { useSelector } from "react-redux"



function DeskU15() {

    const { fifteenthBooler } = useSelector(state => state.fifteenthBooler)
    console.log(useSelector(state => state.fifteenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: fifteenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{fifteenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">15</h5>
      </div>
    </div>
  </div>
  )
}

export default DeskU15
