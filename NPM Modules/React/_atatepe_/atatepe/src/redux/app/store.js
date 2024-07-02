import {configureStore} from "@reduxjs/toolkit"
import boolReducer from "../features/bool/boolSlice"
import secondBoolReducer from "../features/bool/secondBoolSlice"
import thirdBoolReducer from "../features/bool/thirdBoolSlice"
import fourthBoolReducer from "../features/bool/fourthBoolSlice"
import fifthBoolReducer from "../features/bool/fifthBoolSlice"
import sixthBoolReducer from "../features/bool/sixthBoolSlice"
import seventhBoolReducer from "../features/bool/seventhBoolSlice"
import eighthBoolReducer from "../features/bool/eighthBoolSlice"
import ninthBoolReducer from "../features/bool/ninthBoolSlice"
import tenthBoolReducer from "../features/bool/tenthBoolSlice"
import eleventhBoolReducer from "../features/bool/eleventhBoolSlice"
import twelfthBoolReducer from "../features/bool/twelfthBoolSlice"
import thirteenthBoolReducer from "../features/bool/thirteenthBoolSlice"
import fourteenthBoolReducer from "../features/bool/fourteenthBoolSlice"
import fifteenthBoolReducer from "../features/bool/fifteenthBoolSlice"
import sixteenthBoolReducer from "../features/bool/sixteenthBoolSlice"
import seventeenthBoolReducer from "../features/bool/seventeenthBoolSlice"
import eighteenthBoolReducer from "../features/bool/eighteenthBoolSlice"
import nineteenthBoolReducer from "../features/bool/nineteenthBoolSlice"
import twentiethBoolReducer from "../features/bool/twentiethBoolSlice"


export const store = configureStore({
    reducer : {
        booler : boolReducer,
        secondBooler : secondBoolReducer,
        thirdBooler : thirdBoolReducer,
        fourthBooler : fourthBoolReducer,
        fifthBooler : fifthBoolReducer,
        sixthBooler : sixthBoolReducer,
        seventhBooler : seventhBoolReducer,
        eighthBooler : eighthBoolReducer,
        ninthBooler : ninthBoolReducer,
        tenthBooler : tenthBoolReducer,
        eleventhBooler : eleventhBoolReducer,
        twelfthBooler : twelfthBoolReducer,
        thirteenthBooler : thirteenthBoolReducer,
        fourteenthBooler : fourteenthBoolReducer,
        fifteenthBooler : fifteenthBoolReducer,
        sixteenthBooler : sixteenthBoolReducer,
        seventeenthBooler : seventeenthBoolReducer,
        eighteenthBooler : eighteenthBoolReducer,
        nineteenthBooler : nineteenthBoolReducer,
        twentiethBooler : twentiethBoolReducer
    }
})
