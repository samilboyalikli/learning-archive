import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { fourteenthChange } from '../../redux/features/bool/fourteenthBoolSlice'



function Desk14() {

    const dispatch = useDispatch()
    const { fourteenthBooler } = useSelector(state => state.fourteenthBooler)
    console.log(useSelector(state => state.fourteenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: fourteenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{fourteenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">14</h5>
        <button className="btn btn-primary" onClick={() => dispatch(fourteenthChange())}>DEĞİŞTİR</button>
      </div>
    </div>
  </div>
  )
}

export default Desk14
