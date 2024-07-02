import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { eighteenthChange } from '../../redux/features/bool/eighteenthBoolSlice'



function Desk18() {

  const dispatch = useDispatch()
  const { eighteenthBooler } = useSelector(state => state.eighteenthBooler)
  console.log(useSelector(state => state.eighteenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: eighteenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{eighteenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">18</h5>
        <button className="btn btn-primary" onClick={() => dispatch(eighteenthChange())}>DEĞİŞTİR</button>
      </div>
    </div>
  </div>
  )
}

export default Desk18
