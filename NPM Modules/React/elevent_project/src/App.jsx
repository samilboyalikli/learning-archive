import { SiteContextProvider } from './context/SiteContext'
import './index.css';
import CreatePerson from './components/CreatePerson';


function App() {

  return (
    <>
      <SiteContextProvider>
        <CreatePerson />
      </SiteContextProvider>
    </>
  )
}

export default App
