import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    eighteenthBooler : false
}

export const eighteenthBoolSlice = createSlice({
    name : "eighteenthBooler",
    initialState,
    reducers : {
        eighteenthChange : (state) => {
            state.eighteenthBooler = !state.eighteenthBooler
        }
    }
})

export const {eighteenthChange} = eighteenthBoolSlice.actions
export default eighteenthBoolSlice.reducer;
