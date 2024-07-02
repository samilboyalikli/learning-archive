import React from 'react'
import { useSelector } from "react-redux"

function DeskU2() {


  const { secondBooler } = useSelector(state => state.secondBooler)
  console.log(useSelector(state => state.secondBooler))

  return (
    <div>
      <div className="card" style={{ width: '10rem', backgroundColor: secondBooler ? 'red' : 'green', }}>
        <div className="card-top">{secondBooler}</div>
        <div className="card-body text-center">
          <h5 className="card-title text-light fs-1 fw-bold">2</h5>
        </div>
      </div>
    </div>
  )
}

export default DeskU2
