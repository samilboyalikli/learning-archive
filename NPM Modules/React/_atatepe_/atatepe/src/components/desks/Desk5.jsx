import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { fifthChange } from '../../redux/features/bool/fifthBoolSlice'

function Desk5() {

  const dispatch = useDispatch()
  const { fifthBooler } = useSelector(state => state.fifthBooler)
  console.log(useSelector(state => state.fifthBooler))

  return (
    <div>
      <div className="card" style={{ width: '10rem', backgroundColor: fifthBooler ? 'red' : 'green', }}>
        <div className="card-top">{fifthBooler}</div>
        <div className="card-body text-center">
          <h5 className="card-title text-light fs-1 fw-bold">5</h5>
          <button className="btn btn-primary" onClick={() => dispatch(fifthChange())}>DEĞİŞTİR</button>
        </div>
      </div>
    </div>
  )
}

export default Desk5
