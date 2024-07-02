import React from 'react'
import { useSelector } from "react-redux"

function DeskU8() {

    const { eighthBooler } = useSelector(state => state.eighthBooler)
    console.log(useSelector(state => state.eighthBooler))

    return (
        <div>
        <div className="card" style={{ width: '10rem', backgroundColor: eighthBooler ? 'red' : 'green', }}>
          <div className="card-top">{eighthBooler}</div>
          <div className="card-body text-center">
            <h5 className="card-title text-light fs-1 fw-bold">8</h5>
          </div>
        </div>
      </div>
    )
}

export default DeskU8
