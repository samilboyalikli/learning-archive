import { createSlice } from "@reduxjs/toolkit";

export const inputSlice = createSlice({
    name : "input",
    initialState : "",
    reducers : {
        append : (state, action) => {
            return action.payload
        }
    }
})

export const {append} = inputSlice.actions
export default inputSlice.reducer
