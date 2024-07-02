import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { eighthChange } from '../../redux/features/bool/eighthBoolSlice'

function Desk8() {

    const dispatch = useDispatch()
    const { eighthBooler } = useSelector(state => state.eighthBooler)
    console.log(useSelector(state => state.eighthBooler))

    return (
        <div>
        <div className="card" style={{ width: '10rem', backgroundColor: eighthBooler ? 'red' : 'green', }}>
          <div className="card-top">{eighthBooler}</div>
          <div className="card-body text-center">
            <h5 className="card-title text-light fs-1 fw-bold">8</h5>
            <button className="btn btn-primary" onClick={() => dispatch(eighthChange())}>DEĞİŞTİR</button>
          </div>
        </div>
      </div>
    )
}

export default Desk8
