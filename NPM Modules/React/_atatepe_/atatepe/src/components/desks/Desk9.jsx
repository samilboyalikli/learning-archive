import React from 'react'
import { useDispatch, useSelector } from "react-redux"
import { ninthChange } from '../../redux/features/bool/ninthBoolSlice'

function Desk9() {

    const dispatch = useDispatch()
    const { ninthBooler } = useSelector(state => state.ninthBooler)
    console.log(useSelector(state => state.ninthBooler))

    return (
        <div>
        <div className="card" style={{ width: '10rem', backgroundColor: ninthBooler ? 'red' : 'green', }}>
          <div className="card-top">{ninthBooler}</div>
          <div className="card-body text-center">
            <h5 className="card-title text-light fs-1 fw-bold">9</h5>
            <button className="btn btn-primary" onClick={() => dispatch(ninthChange())}>DEĞİŞTİR</button>
          </div>
        </div>
      </div>
    )
}

export default Desk9
