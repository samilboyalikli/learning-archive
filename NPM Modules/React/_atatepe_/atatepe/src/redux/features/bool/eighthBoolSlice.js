import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    eighthBooler : false
}

export const eighthBoolSlice = createSlice({
    name : "eighthBooler",
    initialState,
    reducers : {
        eighthChange : (state) => {
            state.eighthBooler = !state.eighthBooler
        }
    }
})

export const {eighthChange} = eighthBoolSlice.actions
export default eighthBoolSlice.reducer;
