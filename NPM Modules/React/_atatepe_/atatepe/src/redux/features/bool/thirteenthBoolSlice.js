import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    thirteenthBooler : false
}

export const thirteenthBoolSlice = createSlice({
    name : "thirteenthBooler",
    initialState,
    reducers : {
        thirteenthChange : (state) => {
            state.thirteenthBooler = !state.thirteenthBooler
        }
    }
})

export const {thirteenthChange} = thirteenthBoolSlice.actions
export default thirteenthBoolSlice.reducer;
