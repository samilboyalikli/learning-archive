import React, { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { append } from './redux/features/input/inputSlice'
import { secondAppend } from './redux/features/input/secondInputSlice'

function App() {

  const [input, setInput] = useState("")
  const [secondInput, setSecondInput] = useState("")
  const dispatch = useDispatch()

  const handleInputChange = (event) => {
    setInput(event.target.value)
  }
  const secondHandleInputChange = (event) => {
    setSecondInput(event.target.value)
  }

  const boy = () => dispatch(append(input))
  const kilo = () => dispatch(secondAppend(secondInput))
  const saveInputs = () => {
    boy()
    kilo()
  }
  const bmiBoy = useSelector((state) => state.input)
  const bmiKilo = useSelector((state) => state.secondInput)
  const bmi = () => {
    const metreCinsinden = bmiBoy / 100;
    const netBmi = bmiKilo / (metreCinsinden * metreCinsinden);
    return netBmi.toFixed(2)
  }

  return (
    <div className='container text-center'>
      <div className='row'>
        <div className='col'></div>
        <div className='col'>
          <div className="input-group mb-3">
            <span className="input-group-text" id="inputGroup-sizing-default">BOYUNUZ</span>
            <input
              type="text"
              className="form-control"
              aria-label="Sizing example input"
              aria-describedby="inputGroup-sizing-default"
              value={input}
              onChange={handleInputChange}/>
          </div>
          <div className="input-group mb-3">
            <span className="input-group-text" id="inputGroup-sizing-default">KİLONUZ</span>
            <input
              type="text"
              className="form-control"
              aria-label="Sizing example input"
              aria-describedby="inputGroup-sizing-default"
              value={secondInput}
              onChange={secondHandleInputChange}/> <br />
          </div>
          <button className="btn btn-primary" onClick={saveInputs}>KAYDET</button> <br /> <br />
          <div className="input-group mb-3">
            <span className="input-group-text" id="inputGroup-sizing-default">BOY KİLO ENDEKSİNİZ: </span>
            <div
              type="text"
              className="form-control"
              aria-label="Sizing example input"
              aria-describedby="inputGroup-sizing-default">{bmi()}</div>
          </div>
        </div>
        <div className='col'></div>
      </div>
    </div>
  )
}

export default App
