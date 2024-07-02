import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { nineteenthChange } from '../../redux/features/bool/nineteenthBoolSlice'



function Desk19() {

  const dispatch = useDispatch()
  const { nineteenthBooler } = useSelector(state => state.nineteenthBooler)
  console.log(useSelector(state => state.nineteenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: nineteenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{nineteenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">19</h5>
        <button className="btn btn-primary" onClick={() => dispatch(nineteenthChange())}>DEĞİŞTİR</button>
      </div>
    </div>
  </div>
  )
}

export default Desk19
