import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { sixthChange } from '../../redux/features/bool/sixthBoolSlice'

function Desk6() {

    const dispatch = useDispatch()
    const { sixthBooler } = useSelector(state => state.sixthBooler)
    console.log(useSelector(state => state.sixthBooler))

    return (
        <div>
        <div className="card" style={{ width: '10rem', backgroundColor: sixthBooler ? 'red' : 'green', }}>
          <div className="card-top">{sixthBooler}</div>
          <div className="card-body text-center">
            <h5 className="card-title text-light fs-1 fw-bold">6</h5>
            <button className="btn btn-primary" onClick={() => dispatch(sixthChange())}>DEĞİŞTİR</button>
          </div>
        </div>
      </div>
    )
}

export default Desk6
