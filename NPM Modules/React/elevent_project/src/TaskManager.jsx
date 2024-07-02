import React, { useContext, useState } from "react";
import { SiteContext } from "./context/SiteContext";
import { Add, Change, Delete } from "./reducer/task";
import { NewInput, DeleteButton, NewCheckBox, AddButton, HeaderH2, NewHeader } from "./components/styled/StyledElement";
import { LuClipboardList } from "react-icons/lu";
import { BsFillXCircleFill } from "react-icons/bs";
import { BsFillPlusCircleFill } from "react-icons/bs";

function TaskManager({ person }) {
  const { state, dispatch } = useContext(SiteContext);
  const personTasks = state.personalTasks[person.id] || [];
  console.log(person.id)
  const [newTask, setNewTask] = useState('');

  const addTask = () => {
    if (newTask.trim() !== '') {
      dispatch({ type: Add, payload: { text: newTask, personId: person.id } });      
      setNewTask('');
    }
  };

  const changeTask = taskId => {
    dispatch({ type: Change, payload: { personId: person.id, taskId } });
  };

  const deleteTask = taskId => {
    dispatch({ type: Delete, payload: { personId: person.id, taskId } });
  };

  return (
    <>
      <div className="taskContent">
        <ul>
        {personTasks.map((task, index) => (
            <li key={index} className="taskLi">
              <NewCheckBox
                type="checkbox"
                checked={task.completed}
                onChange={() => changeTask(task.id)}
              />              
              <span style={{ textDecoration: task.completed ? 'line-through' : 'none' }}>
                {task.text}
              </span>
              <DeleteButton onClick={() => deleteTask(task.id)}><BsFillXCircleFill /></DeleteButton>
            </li>
          ))}
        </ul>
        <div>
          <NewInput
            type="text"
            value={newTask}
            onChange={e => setNewTask(e.target.value)}
            placeholder="Verilecek Görevi Yazınız"
          />
          <AddButton onClick={addTask}><BsFillPlusCircleFill /></AddButton>
        </div>
      </div>
    </>
  );
}

export default TaskManager;