import { Add, Delete, Change, Clear } from "./actionType";

export const InitialState= {
    tasks: [],
    personalTasks: {} 
}

export const taskReducer = (state, action) => {
    switch(action.type){
        case Add:
            const personId = action.payload.personId;
            const newTask = { id: Date.now(), text: action.payload.text, completed: false };

            const updatedPersonalTasks = state.personalTasks[personId] || [];
            
            return {
                ...state,
                personalTasks: {
                    ...state.personalTasks,
                    [personId]: [...updatedPersonalTasks, newTask],
                },
            };
        case Delete:
            const personIdToDelete = action.payload.personId;
            const taskIdToDelete = action.payload.taskId;

            if (!state.personalTasks[personIdToDelete]) {
                return state;
            }

            const updatedTasksAfterDelete = state.personalTasks[personIdToDelete].filter(
                task => task.id !== taskIdToDelete
            );

            return {
                ...state,
                personalTasks: {
                    ...state.personalTasks,
                    [personIdToDelete]: updatedTasksAfterDelete,
                },
            };
        case Change:
            const personIdToChange = action.payload.personId;
            const taskIdToChange = action.payload.taskId;

            if (!state.personalTasks[personIdToChange]) {
                return state;
            }

            const updatedTaskStatus = state.personalTasks[personIdToChange].map(
                task =>
                    task.id === taskIdToChange
                        ? { ...task, completed: !task.completed }
                        : task
            );

            return {
                ...state,
                personalTasks: {
                    ...state.personalTasks,
                    [personIdToChange]: updatedTaskStatus,
                },
            };
        default:
            return state;            
    }
};