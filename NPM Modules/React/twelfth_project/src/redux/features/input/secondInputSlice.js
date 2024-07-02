import { createSlice } from "@reduxjs/toolkit";

export const secondInputSlice = createSlice({
    name : "secondInput",
    initialState : "",
    reducers : {
        secondAppend : (state, action) => {
            return action.payload
        }
    }
})

export const {secondAppend} = secondInputSlice.actions
export default secondInputSlice.reducer
