import React from 'react'
import { useSelector } from "react-redux"

function DeskU7() {

    const { seventhBooler } = useSelector(state => state.seventhBooler)
    console.log(useSelector(state => state.seventhBooler))

    return (
        <div>
        <div className="card" style={{ width: '10rem', backgroundColor: seventhBooler ? 'red' : 'green', }}>
          <div className="card-top">{seventhBooler}</div>
          <div className="card-body text-center">
            <h5 className="card-title text-light fs-1 fw-bold">7</h5>
          </div>
        </div>
      </div>
    )
}

export default DeskU7
