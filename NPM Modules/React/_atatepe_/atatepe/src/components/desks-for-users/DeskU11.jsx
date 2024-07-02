import React from 'react'
import { useSelector } from "react-redux"



function DeskU11() {

    const { eleventhBooler } = useSelector(state => state.eleventhBooler)
    console.log(useSelector(state => state.eleventhBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: eleventhBooler ? 'red' : 'green', }}>
      <div className="card-top">{eleventhBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">11</h5>
      </div>
    </div>
  </div>
  )
}

export default DeskU11
