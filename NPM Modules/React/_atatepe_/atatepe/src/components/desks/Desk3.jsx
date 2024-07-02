import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { thirdChange } from '../../redux/features/bool/thirdBoolSlice'

function Desk3() {

  const dispatch = useDispatch()
  const { thirdBooler } = useSelector(state => state.thirdBooler)
  console.log(useSelector(state => state.thirdBooler))

  return (
    <div>
      <div className="card" style={{ width: '10rem', backgroundColor: thirdBooler ? 'red' : 'green', }}>
        <div className="card-top">{thirdBooler}</div>
        <div className="card-body text-center">
          <h5 className="card-title text-light fs-1 fw-bold">3</h5>
          <button className="btn btn-primary" onClick={() => dispatch(thirdChange())}>DEĞİŞTİR</button>
        </div>
      </div>
    </div>
  )
}

export default Desk3
