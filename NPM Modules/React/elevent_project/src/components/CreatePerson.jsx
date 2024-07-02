import React, { useState } from "react";
import TaskManager from "../TaskManager";
import { NewButton, HeaderH2, NewInput, NameHeader } from "./styled/StyledElement";
import { BsFillPlusCircleFill } from "react-icons/bs";

const CreatePerson = () => {
  const [newPersonName, setNewPersonName] = useState("");
  const [persons, setPersons] = useState([]);
  const [task, setTask] = useState("boş");
  const [selectedPerson, setSelectedPerson] = useState(null);

  const handleCreatePerson = () => {
    if (newPersonName.trim() !== "") {
      const newPerson = { id: persons.length + 1, name: newPersonName, tasks: task };
      setPersons([...persons, newPerson]);
      setTask([...task, `Task for ${newPersonName}`]);

      setNewPersonName("");
    }  
  };



  return (
    <div className="container">
      <NewInput
        type="text"
        value={newPersonName}
        onChange={(e) => setNewPersonName(e.target.value)}
        placeholder="Görev Verilecek Kişiyi Yazınız"
      />
      <NewButton onClick={handleCreatePerson}><BsFillPlusCircleFill /></NewButton>
      
      {persons.map((person, index) => (
        <li key={index} className="personLi">
          
           <NameHeader> {person.name} </NameHeader>
          
          <TaskManager person={person}/>
        </li>
      ))}
      {selectedPerson && (
        
        <div>
          <HeaderH2>{selectedPerson.name}</HeaderH2>
          <div>            
            
          </div>
        </div>
      )}

    </div>
  );
};

export default CreatePerson;
