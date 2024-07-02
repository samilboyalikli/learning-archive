import { createContext, useReducer } from "react";
import { InitialState, taskReducer } from "../reducer/task";


const SiteContext = createContext()

function SiteContextProvider({children}){    
    const [tasks, taskDispatch] = useReducer(taskReducer, InitialState)  
    const context = {state:tasks, dispatch:taskDispatch}

    return <SiteContext.Provider value={context}>
        {children}
    </SiteContext.Provider>
}


export {SiteContextProvider, SiteContext, }