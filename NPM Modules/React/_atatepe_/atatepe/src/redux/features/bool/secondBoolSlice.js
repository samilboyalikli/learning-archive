import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    secondBooler : false
}

export const secondBoolSlice = createSlice({
    name : "secondBooler",
    initialState,
    reducers : {
        secondChange : (state) => {
            state.secondBooler = !state.secondBooler
        }
    }
})

export const {secondChange} = secondBoolSlice.actions
export default secondBoolSlice.reducer;
