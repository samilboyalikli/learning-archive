import React from 'react'
import { useSelector } from "react-redux"

function DeskU9() {

    const { ninthBooler } = useSelector(state => state.ninthBooler)
    console.log(useSelector(state => state.ninthBooler))

    return (
        <div>
        <div className="card" style={{ width: '10rem', backgroundColor: ninthBooler ? 'red' : 'green', }}>
          <div className="card-top">{ninthBooler}</div>
          <div className="card-body text-center">
            <h5 className="card-title text-light fs-1 fw-bold">9</h5>
          </div>
        </div>
      </div>
    )
}

export default DeskU9
