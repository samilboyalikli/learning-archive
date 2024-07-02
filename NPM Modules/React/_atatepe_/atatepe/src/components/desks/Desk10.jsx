import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { tenthChange } from '../../redux/features/bool/tenthBoolSlice'

function Desk10() {

    const dispatch = useDispatch()
    const { tenthBooler } = useSelector(state => state.tenthBooler)
    console.log(useSelector(state => state.tenthBooler))

    return (
        <div>
        <div className="card" style={{ width: '10rem', backgroundColor: tenthBooler ? 'red' : 'green', }}>
          <div className="card-top">{tenthBooler}</div>
          <div className="card-body text-center">
            <h5 className="card-title text-light fs-1 fw-bold">10</h5>
            <button className="btn btn-primary" onClick={() => dispatch(tenthChange())}>DEĞİŞTİR</button>
          </div>
        </div>
      </div>
    )
}

export default Desk10
