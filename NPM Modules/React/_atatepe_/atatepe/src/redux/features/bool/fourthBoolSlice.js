import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    fourthBooler : false
}

export const fourthBoolSlice = createSlice({
    name : "fourthBooler",
    initialState,
    reducers : {
        fourthChange : (state) => {
            state.fourthBooler = !state.fourthBooler
        }
    }
})

export const {fourthChange} = fourthBoolSlice.actions
export default fourthBoolSlice.reducer;
