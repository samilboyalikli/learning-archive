import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { fifteenthChange } from '../../redux/features/bool/fifteenthBoolSlice'



function Desk15() {

    const dispatch = useDispatch()
    const { fifteenthBooler } = useSelector(state => state.fifteenthBooler)
    console.log(useSelector(state => state.fifteenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: fifteenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{fifteenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">15</h5>
        <button className="btn btn-primary" onClick={() => dispatch(fifteenthChange())}>DEĞİŞTİR</button>
      </div>
    </div>
  </div>
  )
}

export default Desk15
