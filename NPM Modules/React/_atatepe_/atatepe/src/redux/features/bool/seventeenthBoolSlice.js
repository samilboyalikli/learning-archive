import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    seventeenthBooler : false
}

export const seventeenthBoolSlice = createSlice({
    name : "seventeenthBooler",
    initialState,
    reducers : {
        seventeenthChange : (state) => {
            state.seventeenthBooler = !state.seventeenthBooler
        }
    }
})

export const {seventeenthChange} = seventeenthBoolSlice.actions
export default seventeenthBoolSlice.reducer;
