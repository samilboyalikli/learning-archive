import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    twelfthBooler : false
}

export const twelfthBoolSlice = createSlice({
    name : "twelfthBooler",
    initialState,
    reducers : {
        twelfthChange : (state) => {
            state.twelfthBooler = !state.twelfthBooler
        }
    }
})

export const {twelfthChange} = twelfthBoolSlice.actions
export default twelfthBoolSlice.reducer;
