import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    eleventhBooler : false
}

export const eleventhBoolSlice = createSlice({
    name : "eleventhBooler",
    initialState,
    reducers : {
        eleventhChange : (state) => {
            state.eleventhBooler = !state.eleventhBooler
        }
    }
})

export const {eleventhChange} = eleventhBoolSlice.actions
export default eleventhBoolSlice.reducer;
