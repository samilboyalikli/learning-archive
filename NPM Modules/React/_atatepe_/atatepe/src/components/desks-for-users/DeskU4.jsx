import React from 'react'
import { useSelector } from "react-redux"

function DeskU4() {

  const { fourthBooler } = useSelector(state => state.fourthBooler)
  console.log(useSelector(state => state.fourthBooler))

  return (
    <div>
      <div className="card" style={{ width: '10rem', backgroundColor: fourthBooler ? 'red' : 'green', }}>
        <div className="card-top">{fourthBooler}</div>
        <div className="card-body text-center">
          <h5 className="card-title text-light fs-1 fw-bold">4</h5>
        </div>
      </div>
    </div>
  )
}

export default DeskU4
