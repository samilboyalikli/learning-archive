import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    ninthBooler : false
}

export const ninthBoolSlice = createSlice({
    name : "ninthBooler",
    initialState,
    reducers : {
        ninthChange : (state) => {
            state.ninthBooler = !state.ninthBooler
        }
    }
})

export const {ninthChange} = ninthBoolSlice.actions
export default ninthBoolSlice.reducer;
