import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    fifthBooler : false
}

export const fifthBoolSlice = createSlice({
    name : "fifthBooler",
    initialState,
    reducers : {
        fifthChange : (state) => {
            state.fifthBooler = !state.fifthBooler
        }
    }
})

export const {fifthChange} = fifthBoolSlice.actions
export default fifthBoolSlice.reducer;
