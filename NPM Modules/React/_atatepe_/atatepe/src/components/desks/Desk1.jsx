import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { change } from '../../redux/features/bool/boolSlice'

function Desk1() {

  const dispatch = useDispatch()
  const { booler } = useSelector(state => state.booler)
  console.log(useSelector(state => state.booler))

  return (
    <div>
      <div className="card" style={{ width: '10rem', backgroundColor: booler ? 'red' : 'green', }}>
        <div className="card-top">{booler}</div>
        <div className="card-body text-center">
          <h5 className="card-title text-light fs-1 fw-bold">1</h5>
          <button className="btn btn-primary" onClick={() => dispatch(change())}>DEĞİŞTİR</button>
        </div>
      </div>
    </div>
  )
}

export default Desk1
