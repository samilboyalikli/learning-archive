import React from 'react'
import { useSelector } from "react-redux"



function DeskU14() {

    const { fourteenthBooler } = useSelector(state => state.fourteenthBooler)
    console.log(useSelector(state => state.fourteenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: fourteenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{fourteenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">14</h5>
      </div>
    </div>
  </div>
  )
}

export default DeskU14
