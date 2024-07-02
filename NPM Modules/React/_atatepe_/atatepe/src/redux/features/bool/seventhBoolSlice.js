import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    seventhBooler : false
}

export const seventhBoolSlice = createSlice({
    name : "seventhBooler",
    initialState,
    reducers : {
        seventhChange : (state) => {
            state.seventhBooler = !state.seventhBooler
        }
    }
})

export const {seventhChange} = seventhBoolSlice.actions
export default seventhBoolSlice.reducer;
