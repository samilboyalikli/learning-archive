import React from 'react'
import { useSelector } from "react-redux"



function DeskU17() {

  const { seventeenthBooler } = useSelector(state => state.seventeenthBooler)
  console.log(useSelector(state => state.seventeenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: seventeenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{seventeenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">17</h5>
      </div>
    </div>
  </div>
  )
}

export default DeskU17
