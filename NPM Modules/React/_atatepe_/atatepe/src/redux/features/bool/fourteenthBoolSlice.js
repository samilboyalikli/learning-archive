import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    fourteenthBooler : false
}

export const fourteenthBoolSlice = createSlice({
    name : "fourteenthBooler",
    initialState,
    reducers : {
        fourteenthChange : (state) => {
            state.fourteenthBooler = !state.fourteenthBooler
        }
    }
})

export const {fourteenthChange} = fourteenthBoolSlice.actions
export default fourteenthBoolSlice.reducer;
