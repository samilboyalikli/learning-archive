import { configureStore } from "@reduxjs/toolkit";
import inputSlice from "../features/input/inputSlice";
import secondInputSlice from "../features/input/secondInputSlice";


export const store = configureStore({
  reducer : {
      input : inputSlice,
      secondInput : secondInputSlice
  }
})
