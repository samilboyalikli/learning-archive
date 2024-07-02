import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { eleventhChange } from '../../redux/features/bool/eleventhBoolSlice'



function Desk11() {

    const dispatch = useDispatch()
    const { eleventhBooler } = useSelector(state => state.eleventhBooler)
    console.log(useSelector(state => state.eleventhBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: eleventhBooler ? 'red' : 'green', }}>
      <div className="card-top">{eleventhBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">11</h5>
        <button className="btn btn-primary" onClick={() => dispatch(eleventhChange())}>DEĞİŞTİR</button>
      </div>
    </div>
  </div>
  )
}

export default Desk11
