import { useState } from 'react'
import FileUpload from './components/FileUpload'
import TextEditor from './components/TextEditor'
import './App.css'

function App() {
  const [fileContent,setFileContent] = useState('')
  return (<>
    
    { fileContent ? 
    <TextEditor fileContent={fileContent}/> :
    <FileUpload setFileContent={setFileContent}/>}
  </>)
}

export default App
