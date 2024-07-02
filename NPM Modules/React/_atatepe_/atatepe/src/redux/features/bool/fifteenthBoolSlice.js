import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    fifteenthBooler : false
}

export const fifteenthBoolSlice = createSlice({
    name : "fifteenthBooler",
    initialState,
    reducers : {
        fifteenthChange : (state) => {
            state.fifteenthBooler = !state.fifteenthBooler
        }
    }
})

export const {fifteenthChange} = fifteenthBoolSlice.actions
export default fifteenthBoolSlice.reducer;
