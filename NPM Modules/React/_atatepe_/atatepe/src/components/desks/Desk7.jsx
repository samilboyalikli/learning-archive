import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { seventhChange } from '../../redux/features/bool/seventhBoolSlice'

function Desk7() {

    const dispatch = useDispatch()
    const { seventhBooler } = useSelector(state => state.seventhBooler)
    console.log(useSelector(state => state.seventhBooler))

    return (
        <div>
        <div className="card" style={{ width: '10rem', backgroundColor: seventhBooler ? 'red' : 'green', }}>
          <div className="card-top">{seventhBooler}</div>
          <div className="card-body text-center">
            <h5 className="card-title text-light fs-1 fw-bold">7</h5>
            <button className="btn btn-primary" onClick={() => dispatch(seventhChange())}>DEĞİŞTİR</button>
          </div>
        </div>
      </div>
    )
}

export default Desk7
