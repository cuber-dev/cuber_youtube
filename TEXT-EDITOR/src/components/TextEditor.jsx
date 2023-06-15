import { useState } from "react";
import DownloadWindow from "./DownloadWindow";


function TextEditor({ fileContent }) {
    const [content,setContent] = useState(fileContent)
    const [isSubmitted,setIsSubmitted] = useState(false)
    function handleSubmit(e){
        e.preventDefault()
        setIsSubmitted(true)
    }
    return ( <>
        <h1 className="heading">Text Editor</h1>
        <div className="editor-container">
            <form>
                <textarea
                name="" 
                id="text-area" 
                cols="30" 
                rows="12" 
                value={content}
                onChange={(e) => setContent(e.target.value)}
                >
                </textarea>
                <button type="submit" className="btn" onClick={handleSubmit}>Submit</button>
            </form>
        </div>
        { isSubmitted ? <DownloadWindow content={content} setIsSubmitted={setIsSubmitted}/> : ''}
    </> );
}

export default TextEditor;