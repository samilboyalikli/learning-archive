import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    nineteenthBooler : false
}

export const nineteenthBoolSlice = createSlice({
    name : "nineteenthBooler",
    initialState,
    reducers : {
        nineteenthChange : (state) => {
            state.nineteenthBooler = !state.nineteenthBooler
        }
    }
})

export const {nineteenthChange} = nineteenthBoolSlice.actions
export default nineteenthBoolSlice.reducer;
