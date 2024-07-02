import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    tenthBooler : false
}

export const tenthBoolSlice = createSlice({
    name : "tenthBooler",
    initialState,
    reducers : {
        tenthChange : (state) => {
            state.tenthBooler = !state.tenthBooler
        }
    }
})

export const {tenthChange} = tenthBoolSlice.actions
export default tenthBoolSlice.reducer;
