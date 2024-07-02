import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    sixteenthBooler : false
}

export const sixteenthBoolSlice = createSlice({
    name : "sixteenthBooler",
    initialState,
    reducers : {
        sixteenthChange : (state) => {
            state.sixteenthBooler = !state.sixteenthBooler
        }
    }
})

export const {sixteenthChange} = sixteenthBoolSlice.actions
export default sixteenthBoolSlice.reducer;
