import React from 'react'
import { useSelector } from "react-redux"

function DeskU5() {

  const { fifthBooler } = useSelector(state => state.fifthBooler)
  console.log(useSelector(state => state.fifthBooler))

  return (
    <div>
      <div className="card" style={{ width: '10rem', backgroundColor: fifthBooler ? 'red' : 'green', }}>
        <div className="card-top">{fifthBooler}</div>
        <div className="card-body text-center">
          <h5 className="card-title text-light fs-1 fw-bold">5</h5>
        </div>
      </div>
    </div>
  )
}

export default DeskU5
