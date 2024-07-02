import React from 'react'
import { useSelector } from "react-redux"



function DeskU12() {

    const { twelfthBooler } = useSelector(state => state.twelfthBooler)
    console.log(useSelector(state => state.twelfthBooler))

    return (
      <div>
      <div className="card" style={{ width: '10rem', backgroundColor: twelfthBooler ? 'red' : 'green', }}>
        <div className="card-top">{twelfthBooler}</div>
        <div className="card-body text-center">
          <h5 className="card-title text-light fs-1 fw-bold">12</h5>
        </div>
      </div>
    </div>
    )
}

export default DeskU12
