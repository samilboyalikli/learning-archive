import styled from "styled-components"

export const NewButton = styled.button`
    padding: 0;
    border: none;
    margin: 30px 10px;
    background-color: rgb(30, 30, 30);
    color: white;
    cursor: pointer;
    transition: background-color 0.3s ease;
    font-size: 2em;
    &:hover {
        font-size: 2.2em;
    }
`

export const HeaderH2 = styled.h2`
    text-align: center;
    font-size: 2em;
    border: 2px solid gray;
    padding: 10px;
    background-color: rgb(4, 4, 79);
    width: 450px;
    border-radius: 20px;   
    color: white;

    @media (max-width: 900px) {
        width: 450px;
    }
    @media (max-width: 600px) {
        width: 150px;
    }


  `

export const NewInput = styled.input`
    padding: 8px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 500px;

    @media (max-width: 600px) {
        width: 250px;
    }
`
export const NewCheckBox = styled.input`
    appearance: none;
    width: 20px;
    height: 20px;
    border: 1px solid black;
    border-radius: 8px;
    margin-right: 8px;
    margin-top: 10px;
    cursor: pointer;
    background-color: #b8250f;

    &:checked {
        background-color: #30b512;
    }
`

export const DeleteButton = styled.button`
    padding: 6px 20px;
    border: none;
    border-radius: 6px;
    margin-left: 50px;
    background-color: rgb(30,30,30);
    color: white;
    cursor: pointer;
    font-size: 1em;
    &:hover {
        font-size: 1.5em;
    }
`
export const AddButton = styled.button`
    padding: 6px 20px;
    border: none;
    border-radius: 6px;
    margin-left: 50px;
    background-color: rgb(30,30,30);
    color: white;
    cursor: pointer;
    font-size: 1em;
    &:hover {
        font-size: 1.5em;
    }
`

export const NameHeader = styled.h2`
    text-align: center;
    font-size: 1.5em;
    font-family: Arial, sans-serif;
    border: 2px gray;
    border-radius: 10px;
    padding: 30px;
    background-color: black;
    width: 92%;  
    color: white;

    @media (max-width: 900px) {
        width: 150px;
    }
    @media (max-width: 600px) {
        width: 125px;
        display: grid;
        place-items: center;
    }
`

export const NewHeader = styled.h2`
    text-align: center;
    font-size: 2em;
    border: 2px solid gray;
    padding: 5px;
    background-color: rgb(4, 4, 79);
    border-radius: 20px;
    width: 550px;  
    color: white;

    @media (max-width: 900px) {
        width: 150px;
    }
    @media (max-width: 600px) {
        width: 125px;
        display: grid;
        place-items: center;
    }
`