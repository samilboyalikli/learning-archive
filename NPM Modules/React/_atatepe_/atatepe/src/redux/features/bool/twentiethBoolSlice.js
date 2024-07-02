import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    twentiethBooler : false
}

export const twentiethBoolSlice = createSlice({
    name : "twentiethBooler",
    initialState,
    reducers : {
        twentiethChange : (state) => {
            state.twentiethBooler = !state.twentiethBooler
        }
    }
})

export const {twentiethChange} = twentiethBoolSlice.actions
export default twentiethBoolSlice.reducer;
