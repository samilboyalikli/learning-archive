import React from 'react'
import { useSelector } from "react-redux"

function DeskU1() {

  const { booler } = useSelector(state => state.booler)
  console.log(useSelector(state => state.booler))

  return (
    <div>
      <div className="card" style={{ width: '10rem', backgroundColor: booler ? 'red' : 'green', }}>
        <div className="card-top">{booler}</div>
        <div className="card-body text-center">
          <h5 className="card-title text-light fs-1 fw-bold">1</h5>
        </div>
      </div>
    </div>
  )
}

export default DeskU1
