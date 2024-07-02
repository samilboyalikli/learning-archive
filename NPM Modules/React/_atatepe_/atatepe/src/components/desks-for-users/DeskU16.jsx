import React from 'react'
import { useSelector } from "react-redux"



function DeskU16() {

  const { sixteenthBooler } = useSelector(state => state.sixteenthBooler)
  console.log(useSelector(state => state.sixteenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: sixteenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{sixteenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">16</h5>
      </div>
    </div>
  </div>
  )
}

export default DeskU16
