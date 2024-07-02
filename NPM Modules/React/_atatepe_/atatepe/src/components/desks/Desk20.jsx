import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { twentiethChange } from '../../redux/features/bool/twentiethBoolSlice'



function Desk20() {

  const dispatch = useDispatch()
  const { twentiethBooler } = useSelector(state => state.twentiethBooler)
  console.log(useSelector(state => state.twentiethBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: twentiethBooler ? 'red' : 'green', }}>
      <div className="card-top">{twentiethBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">20</h5>
        <button className="btn btn-primary" onClick={() => dispatch(twentiethChange())}>DEĞİŞTİR</button>
      </div>
    </div>
  </div>
  )
}

export default Desk20
