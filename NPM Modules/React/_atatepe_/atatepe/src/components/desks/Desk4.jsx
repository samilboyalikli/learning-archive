import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { fourthChange } from '../../redux/features/bool/fourthBoolSlice'

function Desk4() {

  const dispatch = useDispatch()
  const { fourthBooler } = useSelector(state => state.fourthBooler)
  console.log(useSelector(state => state.fourthBooler))

  return (
    <div>
      <div className="card" style={{ width: '10rem', backgroundColor: fourthBooler ? 'red' : 'green', }}>
        <div className="card-top">{fourthBooler}</div>
        <div className="card-body text-center">
          <h5 className="card-title text-light fs-1 fw-bold">4</h5>
          <button className="btn btn-primary" onClick={() => dispatch(fourthChange())}>DEĞİŞTİR</button>
        </div>
      </div>
    </div>
  )
}

export default Desk4
