import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { secondChange } from '../../redux/features/bool/secondBoolSlice'

function Desk2() {

  const dispatch = useDispatch()
  const { secondBooler } = useSelector(state => state.secondBooler)
  console.log(useSelector(state => state.secondBooler))

  return (
    <div>
      <div className="card" style={{ width: '10rem', backgroundColor: secondBooler ? 'red' : 'green', }}>
        <div className="card-top">{secondBooler}</div>
        <div className="card-body text-center">
          <h5 className="card-title text-light fs-1 fw-bold">2</h5>
          <button className="btn btn-primary" onClick={() => dispatch(secondChange())}>DEĞİŞTİR</button>
        </div>
      </div>
    </div>
  )
}

export default Desk2
