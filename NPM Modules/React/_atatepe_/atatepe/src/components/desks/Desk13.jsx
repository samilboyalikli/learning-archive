import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { thirteenthChange } from '../../redux/features/bool/thirteenthBoolSlice'



function Desk13() {

    const dispatch = useDispatch()
    const { thirteenthBooler } = useSelector(state => state.thirteenthBooler)
    console.log(useSelector(state => state.thirteenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: thirteenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{thirteenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">13</h5>
        <button className="btn btn-primary" onClick={() => dispatch(thirteenthChange())}>DEĞİŞTİR</button>
      </div>
    </div>
  </div>
  )
}

export default Desk13
