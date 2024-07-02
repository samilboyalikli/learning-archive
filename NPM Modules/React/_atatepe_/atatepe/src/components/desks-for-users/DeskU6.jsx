import React from 'react'
import { useSelector } from "react-redux"

function DeskU6() {

    const { sixthBooler } = useSelector(state => state.sixthBooler)
    console.log(useSelector(state => state.sixthBooler))

    return (
        <div>
        <div className="card" style={{ width: '10rem', backgroundColor: sixthBooler ? 'red' : 'green', }}>
          <div className="card-top">{sixthBooler}</div>
          <div className="card-body text-center">
            <h5 className="card-title text-light fs-1 fw-bold">6</h5>
          </div>
        </div>
      </div>
    )
}

export default DeskU6
