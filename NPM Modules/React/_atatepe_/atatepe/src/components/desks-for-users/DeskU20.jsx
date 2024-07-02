import React from 'react'
import { useSelector } from "react-redux"



function DeskU20() {

  const { twentiethBooler } = useSelector(state => state.twentiethBooler)
  console.log(useSelector(state => state.twentiethBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: twentiethBooler ? 'red' : 'green', }}>
      <div className="card-top">{twentiethBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">20</h5>
      </div>
    </div>
  </div>
  )
}

export default DeskU20
