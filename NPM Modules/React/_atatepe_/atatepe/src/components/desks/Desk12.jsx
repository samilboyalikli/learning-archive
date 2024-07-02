import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { twelfthChange } from '../../redux/features/bool/twelfthBoolSlice'



function Desk12() {

    const dispatch = useDispatch()
    const { twelfthBooler } = useSelector(state => state.twelfthBooler)
    console.log(useSelector(state => state.twelfthBooler))

    return (
      <div>
      <div className="card" style={{ width: '10rem', backgroundColor: twelfthBooler ? 'red' : 'green', }}>
        <div className="card-top">{twelfthBooler}</div>
        <div className="card-body text-center">
          <h5 className="card-title text-light fs-1 fw-bold">12</h5>
          <button className="btn btn-primary" onClick={() => dispatch(twelfthChange())}>DEĞİŞTİR</button>
        </div>
      </div>
    </div>
    )
}

export default Desk12
