import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { seventeenthChange } from '../../redux/features/bool/seventeenthBoolSlice'



function Desk17() {

  const dispatch = useDispatch()
  const { seventeenthBooler } = useSelector(state => state.seventeenthBooler)
  console.log(useSelector(state => state.seventeenthBooler))

  return (
    <div>
    <div className="card" style={{ width: '10rem', backgroundColor: seventeenthBooler ? 'red' : 'green', }}>
      <div className="card-top">{seventeenthBooler}</div>
      <div className="card-body text-center">
        <h5 className="card-title text-light fs-1 fw-bold">17</h5>
        <button className="btn btn-primary" onClick={() => dispatch(seventeenthChange())}>DEĞİŞTİR</button>
      </div>
    </div>
  </div>
  )
}

export default Desk17
