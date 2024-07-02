import React from 'react'
import { useSelector } from "react-redux"

function DeskU10() {

    const { tenthBooler } = useSelector(state => state.tenthBooler)
    console.log(useSelector(state => state.tenthBooler))

    return (
        <div>
        <div className="card" style={{ width: '10rem', backgroundColor: tenthBooler ? 'red' : 'green', }}>
          <div className="card-top">{tenthBooler}</div>
          <div className="card-body text-center">
            <h5 className="card-title text-light fs-1 fw-bold">10</h5>
          </div>
        </div>
      </div>
    )
}

export default DeskU10
