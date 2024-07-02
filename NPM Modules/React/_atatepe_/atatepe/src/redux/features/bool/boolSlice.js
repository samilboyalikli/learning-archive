import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    booler : false
}

export const boolSlice = createSlice({
    name : "booler",
    initialState,
    reducers : {
        change : (state) => {
            state.booler = !state.booler
        }
    }
})

export const {change} = boolSlice.actions
export default boolSlice.reducer;
