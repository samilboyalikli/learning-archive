import { createGlobalStyle } from "styled-components";


export const GlobalStyle = createGlobalStyle`
        .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    }

    ul {
    list-style-type: none;
    padding: 0;
    }

    li {
    margin-bottom: 10px;
    }

    .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    }

    @media (max-width: 600px) {
    .task-manager-container {
        padding: 10px;
    }

    .add-task-container {
        flex-direction: column;
        align-items: flex-start;
    }
    }

`