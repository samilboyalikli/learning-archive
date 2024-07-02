import React from 'react'
import { useSelector } from "react-redux"


function DeskU19() {

  const { nineteenthBooler } = useSelector(state => state.nineteenthBooler)
  console.log(useSelector(state => state.nineteenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: nineteenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{nineteenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">19</h5>
      </div>
    </div>
  </div>
  )
}

export default DeskU19
