import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    sixthBooler : false
}

export const sixthBoolSlice = createSlice({
    name : "sixthBooler",
    initialState,
    reducers : {
        sixthChange : (state) => {
            state.sixthBooler = !state.sixthBooler
        }
    }
})

export const {sixthChange} = sixthBoolSlice.actions
export default sixthBoolSlice.reducer;
