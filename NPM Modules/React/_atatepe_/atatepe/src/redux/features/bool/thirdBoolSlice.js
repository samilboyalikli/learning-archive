import {createSlice} from "@reduxjs/toolkit"

const initialState = {
    thirdBooler : false
}

export const thirdBoolSlice = createSlice({
    name : "thirdBooler",
    initialState,
    reducers : {
        thirdChange : (state) => {
            state.thirdBooler = !state.thirdBooler
        }
    }
})

export const {thirdChange} = thirdBoolSlice.actions
export default thirdBoolSlice.reducer
