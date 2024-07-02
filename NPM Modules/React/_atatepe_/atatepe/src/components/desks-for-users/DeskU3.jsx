import React from 'react'
import { useSelector } from "react-redux"

function DeskU3() {

  const { thirdBooler } = useSelector(state => state.thirdBooler)
  console.log(useSelector(state => state.thirdBooler))

  return (
    <div>
      <div className="card" style={{ width: '10rem', backgroundColor: thirdBooler ? 'red' : 'green', }}>
        <div className="card-top">{thirdBooler}</div>
        <div className="card-body text-center">
          <h5 className="card-title text-light fs-1 fw-bold">3</h5>
        </div>
      </div>
    </div>
  )
}

export default DeskU3
